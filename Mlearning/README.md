<img width="470" height="398" alt="image" src="https://github.com/user-attachments/assets/3bc872e4-6ec2-4cef-aebf-17224a55931e" /># 학습 습관 기반 성적 예측 시스템
### 프로젝트 개요

- 학생의 다양한 학습 습관과 생활 패턴을 분석하여 시험 성적을 예측하는 머신러닝 기반 예측 시스템.

## <span id="3">📅 개발 일정</span>

### 프로젝트 개발 기간 : 2025.05.26 - 2025.05.28 ( 총 3 일 )


## <span id="3">📅 개발 스택</span>
<div align="center">
    <img src="https://github.com/user-attachments/assets/34883c5c-f04d-4be0-99c4-200c3572ce15" width="40%">
</div>

<div align="center">
    <img src="https://github.com/user-attachments/assets/427f7f53-d53b-46cb-b1d8-6ac85bbd62b8" width="40%">
</div>

<div align="center">
<img src="https://github.com/user-attachments/assets/9db504f9-ee56-41fc-bca5-63b5c5fa12fb" />
</div>

### 
<br>

# 🛠️ 주요기능
### 개인 학습 / 습관 입력

Streamlit UI를 통한 개인 데이터에 기반한 학습 성적 예측 가능<br>
  <br>
  <div align="center">
    <img src="https://github.com/user-attachments/assets/f208d94a-b653-4641-aefb-3a9088b2d1c4" width="45%">
  </div>

<br><br>

# 🛠️ 기술적 주안점


"개발 초기에는 모든 모델 학습을 순차적으로 처리했지만, 학습 데이터가 많아질수록 학습 시간이 너무 오래 걸리고 사용자가 결과를 기다리기 힘들다는 문제를 경험했습니다. 
이를 해결하기 위해 RandomForest와 GridSearchCV 모두에 병렬 처리(n_jobs=-1)를 적용하여 CPU 멀티코어를 최대한 활용<br>
  <br> 또한 단순히 train-test split으로만 모델을 검증하는것보다 실제 서비스에서는 특정 데이터에만 잘 맞는 과적합 문제와 예측 결과의 신뢰도가 떨어진다는 문제를 경험. 
  이를 해결하기 위해 교차검증(Cross-Validation)과 홀드아웃 검증을 동시에 적용하여 모델의 일반화 성능을 다각도로 검증"<br>
  <br>
  <div align="center">
    <img src="https://github.com/user-attachments/assets/94190fbb-b4f1-4ec8-aa35-5bcf311f3b16" width="70%">
  </div>

   <div align="center">
    <img src="https://github.com/user-attachments/assets/7a6857e9-e01c-4e17-be26-0071c95b8e04" width="70%">
  </div>
  
  # 🛠️ 개발 관련 고민거리


개발 초기에는 결과 페이지에서 시간 계산이 '2.75시간'처럼 소수점으로 표시되어 사용자가 실제 운동 계획을 세우기 어렵고, 성별이나 입력한 음식 정보가 결과에서 확인되지 않아 계산 근거를 알 수 없다는 문제를 경험. 
이를 해결하기 위해 Jinja2 템플릿의 수학 연산 기능을 활용해 '2시간 45분'으로 정확히 변환하고, 성별과 음식 종류 정보를 결과에 명시하여 투명성을 확보.<br>
  <br> 특히 개발하면서 '사용자가 결과를 보고 실제로 행동할 수 있을까?'를 고민. 그래서 단순히 '운동하세요'가 아니라 '달리기 2시간 30분', '수영 1시간 45분'처럼 구체적인 시간과 운동을 제시. 
  또한 결과 페이지에서 불필요한 성별 선택 UI를 제거하고 계산된 결과만 명확히 표시하여 사용자 혼란을 방지했고 HTML 구조도 표준에 맞게 개선하여 모든 브라우저에서 일관되게 작동하도록 개선.<br>
  <br>

<div align="center">
    <img src="https://github.com/user-attachments/assets/0f37608b-9434-4dbe-a84c-1aa36112956a" width="70%">
  </div>
  
  <div align="center">
    <img src="https://github.com/user-attachments/assets/bb20e791-f45f-41f6-b44c-09bc191200c1" width="70%">
  </div>
