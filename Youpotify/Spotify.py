import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline 
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import accuracy_score
import streamlit as st
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
        
        
# # spotipy 모듈의 주요 클래스들이 있는지 확인
# print("spotipy 모듈 확인:")
# print(f"Spotify 클래스 존재: {hasattr(spotipy, 'Spotify')}")
# print(f"SpotifyOAuth 존재: {hasattr(spotipy, 'SpotifyOAuth')}")

# # 사용 가능한 속성들 확인
# print("\nspotipy 모듈의 주요 속성들:")
# attributes = [attr for attr in dir(spotipy) if not attr.startswith('_')]
# for attr in attributes[:10]:  # 처음 10개만 출력
#     print(f"  {attr}")

# # 기본 Spotify 객체 생성 테스트
# try:
#     sp = spotipy.Spotify()
#     print("✅ Spotify 객체 생성 성공!")
# except Exception as e:
#     print(f"❌ Spotify 객체 생성 실패: {e}")




# def diagnose_spotipy():
#     import sys
#     import os
#     import pkg_resources
#     import subprocess
    
#     print("=== SPOTIPY 진단 리포트 ===\n")
    
#     # Python 기본 정보
#     print(f"Python 버전: {sys.version}")
#     print(f"Python 경로: {sys.executable}")
#     print(f"현재 작업 디렉토리: {os.getcwd()}")
#     print(f"가상환경: {os.environ.get('VIRTUAL_ENV', '없음')}")
    
#     # spotipy import 테스트
#     print("\n--- Import 테스트 ---")
#     try:
        
#         print("✅ spotipy import 성공")
#         print(f"   위치: {spotipy.__file__}")
#         print(f"   버전: {spotipy.__version__}")
#     except ImportError as e:
#         print(f"❌ spotipy import 실패: {e}")
    
#     # 패키지 설치 확인
#     print("\n--- 패키지 설치 확인 ---")
#     try:
#         dist = pkg_resources.get_distribution('spotipy')
#         print(f"✅ spotipy 패키지 발견")
#         print(f"   버전: {dist.version}")
#         print(f"   위치: {dist.location}")
#     except pkg_resources.DistributionNotFound:
#         print("❌ spotipy 패키지를 찾을 수 없음")
    
#     # Python 경로 출력
#     print(f"\n--- Python 모듈 검색 경로 ({len(sys.path)}개) ---")
#     for i, path in enumerate(sys.path, 1):
#         print(f"{i:2d}. {path}")

# # 진단 실행
# diagnose_spotipy()

# 판다스 출력 설정
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)  # 너무 많으면 100개 정도로 제한
pd.set_option('display.max_colwidth', 50)  # 너무 길면 50자로 제한
pd.set_option('display.width', None)

# 폰트지정
plt.rcParams['font.family'] = 'Malgun Gothic'

# 마이너스 부호 깨짐 지정
plt.rcParams['axes.unicode_minus'] = False

# 숫자가 지수표현식으로 나올 때 지정
pd.options.display.float_format = '{:.2f}'.format


# 데이터 확인
data = pd.read_csv('./dataset/Spotify Youtube Dataset.csv')
# data.head()
# data.info()

Popularity = data[['Views', 'Stream']]
print("인기 정보:", Popularity)

# print("인기 정보의 결측치:", Popularity.isnull().sum())
# 결측치 제거된 인기 정보
cleaned_popularity = Popularity.dropna()
print("결측치 제거 후 인기 정보:", cleaned_popularity.isnull().sum())

# 유사도만 빼고 제거
droped_data = data.drop(
    ['Artist', 'Url_spotify', 'Track', 'Album', 'Album_type', 'Uri', 
                   'Url_youtube', 'Title', 'Channel', 'Views', 'Likes', 'Comments', 
                   'Description', 'Licensed', 'official_video', 'Stream'], axis=1)

droped_data.head()
# data.info()

# 전처리
# print(droped_data.isnull().sum())

cleaned = droped_data.dropna()
# print("데이터 정리에 결측치까지 없앰", cleaned)

# print("데이터셋 크기:", data.shape)
# print("컬럼 목록:", data.columns.tolist())
# print("결측치 확인:", data.isnull().sum().sum())

# print("결측치 있는지 확인", cleaned['Views'].isnull())

# 숫자가 제각각 : SCaler
scaler = MinMaxScaler(feature_range=(0,1))
scaled = scaler.fit_transform(cleaned)
# scaled_popularity = scaler.fit_transform(cleaned_popularity)
# 스케일링은 한번만
# scaled_test = scaler.transform(cleaned)
print(scaled)
# print("스케일링된 인기도 정보:", scaled_popularity)

# 전처리된 데이터 저장
# spotify = {scaled, columns=cleaned.columns
#            }
similardf = pd.DataFrame(scaled, columns=cleaned.columns)
# similar_popularity = pd.DataFrame(scaled_popularity, columns=cleaned_popularity.columns)
print("스케일링된 데이터프레임:", similardf)
# print("스케일링된 인기 정보 데이터프레임:", similar_popularity)
# df.to_csv('scaled_spotify.csv', index=False)

# 데이터 분할
# X, Y 필요없음

# 모델 및 학습
Nearest = NearestNeighbors(n_neighbors=3)
Nearest.fit(scaled)
# 첫번째 노래의 유사도정보
print("노래", scaled[0])
# 예측 # nearest에는 predict가 없어
# pred_near = Nearst.predict(scaled_test)
# 주요 데이터 : scaled
distances, indices = Nearest.kneighbors([scaled[0]])  # 이 곡의 유사도 정보와 비슷한 곡들 
# 본인 제외
print("유사한 곡들의 '인덱스' :", indices[0][1:])
print("순회", [int(i) for i in indices[0][1:]])
# enumerate로 인덱스와 값을 함께 출력 가능!!!
for idx, value in enumerate(indices[0][1:]):
    print(f"인덱스 {idx}: 값 {value}, 타입 {type(value)}")
# print("분할", np.split(indices, 1, axis=1))
print("거리:", distances)

# 평가
average_distance = distances.mean()
print(f"평균 유사도 거리: {average_distance:.3f}")
# print("모델 성능 평가:")
# print("정확도:", accuracy_score(distances, indices))

# 원본 데이터 사용
# print("선택한 곡:", data.iloc[0]['Track'])
# print("아티스트:", data.iloc[0]['Artist'])

# 시각화
# 1. 정보 표시하기
# 누르면 나올 데이터
def search_song(input_song, data):  
    
    if not input_song:
        return pd.DataFrame()
    
    # 데이터 정리
    # 골라야할 열 지정
    clean_data = data[['Artist', 'Track', 'Album', 'Url_spotify', 'Url_youtube', 'Uri', 'Views', 'Stream']].copy()
                                   # 결측치 제거할 열 지정
    clean_data = clean_data.dropna(subset=['Artist', 'Track', 'Album', 'Url_spotify', 'Url_youtube', 'Uri', 'Views', 'Stream'])
    clean_data = clean_data.drop_duplicates()
    
    intview = clean_data['Views'].astype(int)
    intstream = clean_data['Stream'].astype(int)
    print("정수변환", intview, intstream)
    # print("정리된 데이터:", clean_data)
    # Uri = clean_data['Uri']
    # print("스포티파이 번호:", Uri[0][14:])
    # 입력된 노래 제목 또는 아티스트로 필터링
    # 대소문자 구분 없이 검색
    # 검색한 결과를 반환
    track = clean_data[clean_data['Track'].str.contains(input_song, case=False, na=False)]
    Artist = clean_data[clean_data['Artist'].str.contains(input_song, case=False, na=False)]
    Album = clean_data[clean_data['Album'].str.contains(input_song, case=False, na=False)]
    Url_spotify = clean_data[clean_data['Url_spotify'].str.contains(input_song, case=False, na=False)]
    Url_youtube = clean_data[clean_data['Url_youtube'].str.contains(input_song, case=False, na=False)]
    Views = clean_data[clean_data['Views'].astype(str).str.contains(input_song, case=False, na=False)]
    Stream = clean_data[clean_data['Stream'].astype(str).str.contains(input_song, case=False, na=False)]

    song_inform = pd.concat([track, Artist, Album, Url_spotify, Url_youtube, Views, Stream]).drop_duplicates()
    print("검색된 노래 정보:", song_inform)
    # 열 3개
    # return track[['Track', 'Artist', 'Album']]
    # 열 하나
    # return track[['Track']]  
    return song_inform

# Streamlit 앱
st.markdown(f"""
                    <h1> SPOTIFY&YOUTUBE 기반 노래추천 </h1>


                """, unsafe_allow_html=True)

# print("노래고르기", search_song("Feel", data))

# 검색 스트림릿 입력
# st.text_input(search_song(text_input), data, "노래 제목 또는 아티스트를 입력하세요")
# st.text_input("노래 제목 또는 아티스트를 입력하세요", key="input_song")
text_songs = st.text_input("노래 제목 또는 아티스트를 입력하세요")
# selected_songs = st.selectbox("노래를 선택하세요")

if text_songs:
    # 1. 유사도 이외 노래정보 DF
    search_song_df = search_song(text_songs, data)
    print("검색된 노래 데이터프레임:", search_song_df)
    if not search_song_df.empty:
        # st.write("검색된 노래:")
        # st.dataframe(search_song_df)  
        # 합쳐짐
        
         # 옵션을 문자열로 만들기
        options = []
        # idx와 row는 고유 값 (+value)
        for idx, row in search_song_df.iterrows():
            # sidebar에 표시할 옵션 문자열 생성 (일부)
            # 노래와 아티스트만 표시
            option_text = f"{row['Track']}- {row['Artist']}"
            options.append(option_text)
        print("옵션들:", options)

        # 옵션 정렬
        sorted_options = sorted(options)
        # 여기서 정보 가져오기
        selected_songs = st.selectbox("노래를 선택하세요", options=sorted_options
                                            # .values.tolist(), format_func=lambda x: f"{x[0]} - {x[1]} ({x[2]})"
                                              )
        # 2.전체 목록을 만들고 각 노래에 대한 인덱스를 찾기
        song_options = options.index(selected_songs)
        
        
        
        
        
        
        
        # 0
        print("정보찾기", song_options)
        # Feel good inc
        print("선택한 노래", selected_songs)
        # 선택된 노래의 인덱스에 해당하는 행을 가져오기 (아티스트, 앨범, URL 등)
        selected_song_info = search_song_df.iloc[song_options]
        # 선택된 유사도 노래 정보 (비트, 템포 등)
        choiced_song_info = scaled[song_options].reshape(1, -1)  # 2차원으로 변환 (중요)
        print("선택된 유사도 노래 정보:", choiced_song_info)    
        print("선택된 그 외 노래 정보:", selected_song_info)
    
        
        song_distances, song_indices = Nearest.kneighbors(choiced_song_info)  # 선택된 노래의 유사도 정보
        print("가장 가까운 거리:", song_distances)
        print("유사도:", song_indices[0][1:])  # 첫번째는 자기 자신이므로 제외
        # similar_songs = search_song_df.iloc[indices[:,2:]]
        # print("비슷한 노래들:", similar_songs)
        # print("이게 첫번째", selected_song_info)
        
        # print("선택된 노래:", selected_songs)
        # button = st.button("노래 정보 확인")
        # if selected_songs:
        #     st.selected_songs(f"선택한 노래: {selected_songs}")
        
        # search_page = st.Page("Selected_songs.py"
        #                     , title="선택한 노래"
        #                       )

        # 기존 코드에서 유사한 노래 표시 부분을 이렇게 개선하세요

    if selected_songs:
        
        
        
        Views = selected_song_info['Views']
        Stream = selected_song_info['Stream']
        Uri = selected_song_info['Uri']
        track_name = selected_song_info['Track']
        artist_name = selected_song_info['Artist']
        Album_name = selected_song_info['Album']
        Url_spotify = selected_song_info['Url_spotify']
        Url_youtube = selected_song_info['Url_youtube'] 
        


        # st.metric("조회수", Views.astype(int))
        # st.metric("스트리밍 수", Stream.astype(int))
        
        # # st.line_chart("조회수", Views.astype(int))
        # # st.line_chart("스트리밍 수", Stream.astype(int))
        # df = pd.DataFrame({
        #     '플랫폼': ['YouTube', 'Spotify'],
        #     '수치': [int(selected_song_info['Views']), int(selected_song_info['Stream'])]
        # })

        # st.bar_chart(df.set_index('플랫폼'))


        # col1, col2, col3 = st.columns(3)

        # with col1:
        #     st.metric(
        #         label="🎥 YouTube 조회수",
        #         value=f"{int(selected_song_info['Views']):,}",
        #         delta=None
        #     )

        # with col2:
        #     st.metric(
        #         label="🎧 Spotify 스트리밍",
        #         value=f"{int(selected_song_info['Stream']):,}",
        #         delta=None
        #     )

        # with col3:
        #     total = int(selected_song_info['Views']) + int(selected_song_info['Stream'])
        #     st.metric(
        #         label="📊 총 재생수",
        #         value=f"{total:,}",
        #         delta=None
        #     )
        
        
        
        #Spotify API 사용
        client_id = "8f6acb4451484ca8a290d339e5dad675"
        client_secret = "0f8072cba71a466a97d210485562cfc7"
        
        client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        track_id = Uri[14:]  # 예: '3n3Ppam7vgaVa1iaRUc9Lp'
        track = sp.track(track_id)
        print("선택된 트랙 정보2:", track)
        print("선택된 트랙 정보2:", track['album']['images'])
        
        album_images = track['album']['images']
        if album_images:
        # 가장 큰 이미지 (고화질) 선택
            best_image = album_images[0]['url']  # 640x640
            print("사용할 이미지:", best_image)
        
        
        # for image in track['album']['images']:
        #     print("이미지:", image['url'])

        # st.image(image['url'])

        # 선택한 노래 정보 표시
        # 마크다운 언어
        st.markdown("## 🎵 선택한 노래")
                                   # 첫 번째 열(col1)은 너비 비율 1, 두 번째 열(col2)은 너비 비율 2
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # st.image('./dataset/Gorillaz.jpg', width=150)
            st.image(best_image, width=300)  # 이미지 크기 조정
        
        with col2:
            st.markdown(f"**곡명:** {track_name}")
            st.markdown(f"**아티스트:** {artist_name}")
            st.markdown(f"**앨범:** {Album_name}")
            
            # 링크를 버튼으로 만들기
                                           #동일한 너비를 가지는 2개의 열
            col_spotify, col_youtube = st.columns(2)
            with col_spotify:
                   # Spotify URL이 비어있지 않은 경우에만 링크 표시
                if pd.notna(Url_spotify):
                    st.markdown(f"[🎧 Spotify]({Url_spotify})")
            with col_youtube:
                if pd.notna(Url_youtube):
                    st.markdown(f"[📺 YouTube]({Url_youtube})")
        
        st.divider()  # 구분선
        
        st.markdown(f"""
        <div style="display: flex; gap: 1rem; margin: 1rem 0;">
            <div style="flex: 1; padding: 1rem; background: linear-gradient(45deg, #FF6B6B, #FF8E53); border-radius: 10px; color: white; text-align: center;">
                <h3>🎥 YouTube 조회수</h3>
                <h2>{int(selected_song_info['Views']):,}</h2>
            </div>
            <div style="flex: 1; padding: 1rem; background: linear-gradient(45deg, #1DB954, #1ED760); border-radius: 10px; color: white; text-align: center;">
                <h3>🎧 Spotify 스트리밍</h3>
                <h2>{int(selected_song_info['Stream']):,}</h2>
            </div>
        </div>
        <div style="font-weight: bold;">(2025.7.27 기준)</div>
        """, unsafe_allow_html=True)

        st.divider()




        # 유사한 노래들 표시 - 방법 1: 카드 형태
        st.markdown("## 🎯 추천 노래")
        
        # [i for i in song_indices[0][1:]]에서 정수 변환
        similar_indices = [int(i) for i in song_indices[0][1:]]
        
        # 카드 형태로 표시
        for idx, song_idx in enumerate(similar_indices, 1):
            similar_song = data.iloc[song_idx]
            similarity_score = 1 - song_distances[0][idx]  # 거리를 유사도로 변환

            # st의 "html box" 사용
            with st.container():
                st.markdown(f"""
                <div style="
                    padding: 1rem;
                    border-radius: 10px;
                    border: 1px solid #ddd;
                    margin: 0.5rem 0;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                ">
                    <h4 style="margin: 0 0 0.5rem 0;">🎵 {similar_song['Track']}</h4>
                    <p style="margin: 0.25rem 0;"><strong>👤 아티스트:</strong> {similar_song['Artist']}</p>
                    <p style="margin: 0.25rem 0;"><strong>📀 앨범:</strong> {similar_song['Album']}</p>
                    <p style="margin: 0.25rem 0;"><strong>🎯 유사도:</strong> {similarity_score:.2%}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # 링크 버튼들
                col_spotify, col_youtube, col_space = st.columns([1, 1, 2])
                with col_spotify:
                    # Spotify URL이 비어있지 않은 경우에만 링크 표시
                    # "notna"
                    if pd.notna(similar_song['Url_spotify']):
                        st.markdown(f"[🎧 Spotify]({similar_song['Url_spotify']})")
                with col_youtube:
                    if pd.notna(similar_song['Url_youtube']):
                        st.markdown(f"[📺 YouTube]({similar_song['Url_youtube']})")
                        

st.divider()

# unsafe_allow_html=True > HTML 직접 사용
st.markdown(f"""
                    <h5 style="text-align: center;"> API BY SPOTIFY </h5>


                """, unsafe_allow_html=True)