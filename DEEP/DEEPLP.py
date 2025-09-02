import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    classification_report,
)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
from scipy.stats import zscore
from keras.losses import Huber
import seaborn as sns
import missingno as msno
from sklearn.ensemble import RandomForestRegressor
import streamlit as st
from keras.models import load_model


# 폰트지정
plt.rcParams["font.family"] = "Malgun Gothic"

# 마이너스 부호 깨짐 지정
plt.rcParams["axes.unicode_minus"] = False

# 숫자가 지수표현식으로 나올 때 지정
pd.options.display.float_format = "{:.2f}".format

# 회귀 (예측 모델)
# 1. 데이터 불러오기
file_path = "./dataset/Grocery Price Index Tool.csv"
data = pd.read_csv(file_path)

print(f"데이터 모양: {data.shape}")
print(" 결측치 : ", data.isnull().sum())


# 전처리
# 2. 날짜 처리
data["Date"] = pd.to_datetime(data["Date"])
data.drop("Eggs", axis=1, inplace=True)

# 특정 열 인덱스 설정
data.set_index("Date", inplace=True)
# 정렬 (하는편이 나음)
data.sort_values("Date", inplace=True)


# 3. 결측치 처리 *
# 이전의 유효한 값으로 채우는 방법
data = data.fillna(method="ffill")
# 그리고도 dropna
data.dropna(inplace=True)

msno.matrix(data)  # 이 시점에 시각화


# 이상치 처리
def remove_outliers_zscore(data, threshold=3):
    z_scores = zscore(data)
    abs_z_scores = abs(z_scores)
    filtered_entries = (abs_z_scores < threshold).all(axis=1)
    return data[filtered_entries]


data = remove_outliers_zscore(data)

print(f"처리 후 데이터 : {data.shape}")
data.head()

# 4. 데이터 스케일링
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)


# 5. 시계열 데이터 생성
def create_sequences(data, time_step=10):

    X, y = [], []
    print("길이 :", len(data))
    for i in range(len(data) - time_step):
        X.append(data[i : i + time_step])  # 과거 12개월 데이터
        y.append(data[i + time_step])  # 다음 달 데이터 # X, y구분
    return np.array(X), np.array(y)


time_step = 3
X, y = create_sequences(scaled_data, time_step)

print(f"X 형태: {X.shape}, y 형태: {y.shape}")

# 6. 데이터 분할 (80% 훈련, 20% 테스트)
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

print(f"훈련 데이터: {X_train.shape[0]}, 테스트 데이터: {X_test.shape[0]}")

# 7. GRU 모델 구성 (LSTM보다 빠르고 간단)
model = Sequential(
    [
        # GRU(50, return_sequences=True, input_shape=(time_step, X.shape[2])),
        # Dropout(0.2),
        # GRU(50, return_sequences=False),
        # Dropout(0.2),
        # Dense(25),
        # Dense(X.shape[2])  # 모든 식료품 가격 예측
        GRU(32, return_sequences=False, input_shape=(time_step, X.shape[2])),
        Dropout(0.2),
        Dense(X.shape[2]),
    ]
)

# 8. 모델 컴파일
# 회귀모델 성능 : mse, mae
model.compile(optimizer="adam", loss=Huber(), metrics=["mae"])
model.summary()

# 9. 훈련
early_stop = EarlyStopping(monitor="val_loss", patience=10, restore_best_weights=True)

print("모델 훈련 시작...")
history = model.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.2,  # 훈련 데이터의 20%를 검증용으로
    callbacks=[early_stop],
    verbose=1,
    shuffle=False,
)

# 10. 예측
print("예측 수행...")
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

# 11. 원래 스케일로 복원
train_pred_inv = scaler.inverse_transform(train_pred)
test_pred_inv = scaler.inverse_transform(test_pred)
y_train_inv = scaler.inverse_transform(y_train)
y_test_inv = scaler.inverse_transform(y_test)

# 12. 성능 평가
train_mse = mean_squared_error(y_train_inv, train_pred_inv)
test_mse = mean_squared_error(y_test_inv, test_pred_inv)
train_mae = mean_absolute_error(y_train_inv, train_pred_inv)
test_mae = mean_absolute_error(y_test_inv, test_pred_inv)

print(f"\n=== 모델 성능 ===")
print(f"훈련 MSE: {train_mse:.4f}, MAE: {train_mae:.4f}")
print(f"테스트 MSE: {test_mse:.4f}, MAE: {test_mae:.4f}")

# 모델 저장
md = model.save("model.h5")

# 13. 결과 시각화
plt.figure(figsize=(15, 5))

# 학습 과정
plt.subplot(1, 3, 1)
plt.plot(history.history["loss"], label="Train Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("모델 학습 과정")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()

# 첫 번째 식료품 예측 결과
# 예측값, 테스트값
# print("예측값:" , test_pred_inv[:, 2])
# plt.subplot(1, 3, 2)
# for i in range(test_pred_inv.shape[1]):
#     plt.plot(y_test_inv[:30, i], label=f' {data.columns[i]} 실제값', marker='o')
#     plt.plot(test_pred_inv[:30, i], label=f'{data.columns[i]} 예측값', marker='s')
#     plt.title(f'{data.columns[i]} 예측 결과')
#     plt.xlabel('Time')
#     plt.ylabel('Price Index')
#     plt.legend()

# 각각의 항목들 구분하여
num_columns = test_pred_inv.shape[1]
plt.figure(figsize=(5 * num_columns, 4))  # 그래프 크기 설정

for i in range(num_columns):
    plt.subplot(1, num_columns, i + 1)  # 열 개수만큼 subplot 생성
    plt.plot(y_test_inv[:30, i], label=f"{data.columns[i]} 실제값", marker="o")
    plt.plot(test_pred_inv[:30, i], label=f"{data.columns[i]} 예측값", marker="s")
    plt.title(f"{data.columns[i]} 예측 결과")
    plt.xlabel("기간(일)")
    plt.ylabel("물가지수")
    plt.legend()

plt.tight_layout()
plt.show()

# 전체 성능 (실제 vs 예측)
plt.subplot(1, 3, 3)
plt.scatter(y_test_inv.flatten(), test_pred_inv.flatten(), alpha=0.5)
plt.plot(
    [y_test_inv.min(), y_test_inv.max()], [y_test_inv.min(), y_test_inv.max()], "r--"
)
plt.xlabel("실제값")
plt.ylabel("예측값")
plt.title("실제 vs 예측")

plt.tight_layout()
plt.show()

# 이상치 시각화
errors = np.abs(y_test_inv - test_pred_inv)
plt.figure(figsize=(10, 4))
sns.boxplot(data=errors)
plt.title("오차 분포 (예측 오차)")
plt.xticks(ticks=range(errors.shape[1]), labels=data.columns, rotation=45)
plt.show()

# 1. GRU 입력용 X는 시계열 형태 (3D)이므로, 트리 모델용으로 2D로 바꿔야 합니다.
# 최근 3개월 시점의 마지막 데이터만 사용
X_rf = X.reshape(X.shape[0], -1)
y_rf = y  # y는 그대로

# 트리 기반 회귀 모델 학습
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_rf, y_rf)

# 평균 중요도 계산 (다차원 y일 경우 평균)
importances = rf_model.feature_importances_

# 특성 이름 만들기
# 예: Milk_t-2, Milk_t-1, Milk_t 등
columns = data.columns
feature_names = []
for i in range(time_step):
    for col in columns:
        feature_names.append(f"{col}_t-{time_step - i}")

# 중요도 데이터프레임 생성
importance_df = pd.DataFrame(
    {"특성": feature_names, "중요도": importances}
).sort_values(by="중요도", ascending=False)

# 출력
print(importance_df.head(10))

# 중요도 상위 N개만 선택
top_n = 20
top_features = importance_df["특성"].values[:top_n]

# X_rf를 DataFrame으로 변환
X_rf_df = pd.DataFrame(X_rf, columns=feature_names)

# 상관관계 히트맵 (시간순 정렬된 순수 물품들끼리)
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("식료품 항목 간 상관관계 히트맵")
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()


# 데이터 예시
num_columns = 3
y_test_inv = scaler.inverse_transform(y_test)
test_pred_inv = scaler.inverse_transform(test_pred)

item_names = [
    "Frozen",
    "Grocery",
    "Alcohol",
    "Cheese",
    "Produce",
    "Meat/Alternative Meat",
    "Dairy",
    "Alternative Dairy",
]


st.sidebar.title("딥러닝 물가지수 예측 결과")
st.sidebar.write("원하는 물가지수를 선택해 실제값과 예측값을 비교하세요.")
st.sidebar.write("(2019년 ~ 2025년 5월 현재 기준)")

# 사이드바에서 선택
selected_index = st.sidebar.selectbox("  물가지수 선택", item_names)

st.sidebar.write("Frozen : 냉동 식품")
st.sidebar.write("Grocery : 곡물")
st.sidebar.write("Alcohol : 주류")
st.sidebar.write("Cheese : 치즈")
st.sidebar.write("Produce : 공산품")
st.sidebar.write("Meat/Alternative Meat : 고기류")
st.sidebar.write("Dairy : 유제품")
st.sidebar.write("Alternative Dairy : 대용 유제품")


st.title("🔥한달 간 물가지수")
# 선택한 지수에 대한 그래프 생성
fig, ax = plt.subplots(figsize=(8, 4))
i = data.columns.get_loc(selected_index)
print(i)
ax.plot(
    y_test_inv[:30, i], label=f"{selected_index} 실제값", marker="o", color="#1f77b4"
)
ax.plot(
    test_pred_inv[:30, i], label=f"{selected_index} 예측값", marker="s", color="#ff7f0e"
)
ax.set_title(f"{selected_index} 물가지수 예측 결과")
ax.set_xlabel("기간(일)")
ax.set_ylabel("물가지수")
ax.legend()
ax.grid(True)

# Streamlit에 그래프 표시
st.pyplot(fig)

data2 = pd.DataFrame(
    {
        "한달 전 실제 물가지수": y_test_inv[:1, i],
        "한달 전 예측 물가지수": test_pred_inv[:1, i],
    }
)

data3 = pd.DataFrame(
    {
        "한달 후 실제 물가지수": [y_test_inv[30:, i][-1]],
        "한달 후 예측 물가지수": [test_pred_inv[30:, i][-1]],
    }
)


model = load_model("model.h5")
st.dataframe(data2)
st.dataframe(data3)


# === 연간 평균 ===
st.subheader("📈 연도별 평균 물가지수")
yearly_avg = data.resample("Y").mean()
yearly_avg.index = yearly_avg.index.year  # 연도만 추출

fig1, ax1 = plt.subplots(figsize=(12, 5))
sns.lineplot(data=yearly_avg, ax=ax1)
ax1.set_title("연도별 평균 물가지수 트렌드")
ax1.set_xlabel("연도")
ax1.set_ylabel("평균 물가지수")
ax1.legend(loc="upper left", bbox_to_anchor=(1, 1))
st.pyplot(fig1)

# # === 월간 평균 ===
st.subheader("📅 월별 평균 물가지수")
monthly_avg = data.copy()
monthly_avg["월"] = monthly_avg.index.month
monthly_avg = monthly_avg.groupby("월").mean()

fig2, ax2 = plt.subplots(figsize=(12, 5))
sns.lineplot(data=monthly_avg, ax=ax2)
ax2.set_title("월별 평균 물가지수 (계절성 분석)")
ax2.set_xlabel("월")
ax2.set_ylabel("평균 물가지수")
ax2.set_xticks(range(1, 13))
ax2.legend(loc="upper left", bbox_to_anchor=(1, 1))
st.pyplot(fig2)
