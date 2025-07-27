# 영화정보 챗봇 프로그램
### 프로젝트 개요

- TMDB API와 Ollama LLM을 활용하여 영화 및 드라마 정보를 실시간으로 검색하고 AI가 상세한 설명을 제공하는 웹 기반 챗봇 프로그램입니다.

## <span id="3">📅 개발 일정</span>

### 프로젝트 개발 기간 : 2025.06.16 - 2025.07.11 ( 총 3 일 )


## <span id="3">📅 개발 스택</span>
<div align="center">
    <img src="https://github.com/user-attachments/assets/a33b499c-db3d-4757-90d8-ab6af9219ba0" width="40%">


<div align="center">
    <img src="https://github.com/user-attachments/assets/34883c5c-f04d-4be0-99c4-200c3572ce15" width="40%">
</div>

<div align="center">
    <img src="https://github.com/user-attachments/assets/2c1211d3-499c-4ddc-bdea-b5c6d9e7f0ef" width="40%">
</div>

### 
<br>

# 🛠️ 주요기능
### 궁금한 멀티미디어 항목 입력

사용자가 영화나 드라마 제목을 입력하면 포스터 이미지와 함께 AI가 생성한 맞춤형 콘텐츠 해설을 제공<br>
  <br>
  <div align="center">
    <img src="https://github.com/user-attachments/assets/8e860ead-9e65-4525-8835-6bf47dc0eeb8" width="45%">
  </div>

   <div align="center">
    <img src="https://github.com/user-attachments/assets/15a01b5b-f732-4001-9881-0716c5da7927" width="45%">
  </div>




<br><br>

# 🛠️ 기술적 주안점


 기존 방식에서는 매 요청마다 모델을 새로 로드하는 비효율적인 방식을 사용했으나, 전역 초기화 방식으로 변경하여 애플리케이션 시작 시 한 번만 모델을 메모리에 로드하도록 개선. 
 이를 통해 반복적인 모델 로딩을 제거하여 응답 시간을 대폭 단축. 
 추가로 Ollama 기반의 로컬 LLM을 선택하여 호출당 발생하는 운영 비용을 절약하고 네트워크 지연 시간을 줄여 응답 속도까지 향상.
    
  <br> 초기에는 첫 번째 요청 시 전체 데이터셋을 일괄 로드하는 방식으로 인해 초기 응답 속도가 15-20초까지 지연되는 문제가 발생. 
  이를 해결하기 위해 필요한 첫 번째 데이터만 선택적으로 로드하도록 변경. "<br>

  외부 API의 신뢰성과 로컬 AI의 효율성을 전략적으로 결합 하이브리드 구조를 설계. 
  TMDB API가 실시간 영화 데이터와 포스터를 제공하면, Ollama LLM이 친근한 설명으로 변환하는 방식으로 결과적으로 데이터의 정확성(TMDB) + 설명의 지능성(Ollama) + 비용 효율성(로컬 처리)을 한번에 구현.
  <br>
  <div align="center">
    <img src="https://github.com/user-attachments/assets/9da24307-831f-4f81-bb73-c4ac4aff0a13" width="70%">
  </div>

   <div align="center">
    <img src="https://github.com/user-attachments/assets/a12e10a3-3635-4802-b776-e11c87cea858" width="70%">
  </div>

   <div align="center">
    <img src="https://github.com/user-attachments/assets/949a0566-5778-49fb-ab19-dd81b3bb8b39" width="70%">
  </div>

  # 🛠️ AI 응답 속도 최적화 트러블슈팅


모델 전역 최적화와 선택적 데이터 로드 방식을 통해 지연 속도를 개선하려고 노력했지만, 여전히 프롬프트 불러오는 속도는 사용자들이 불편을 느낄 정도로 길었음. 
이에 추가적인 속도 향상을 위해 첫 번째로 캐싱을 도입하여 반복되는 API 호출 횟수를 한번으로 제한하고 그만큼의 시간을 단축. 
하지만 더 중요한 건 프롬프트를 간소화하는 것이었는데, 이를 통해 기존 180초가 넘던 응답 시간이 절반 이하로 단축.<br>
  <br> 다만, gemma2이외의 모델을 사용하면 응답 생성 실패 등 품질 저하 문제가 발생하였기 때문에, 추가적인 모델 실험과 조합을 통해<br>
  더욱 향상된 성능을 찾을 계획<br>
  <br>

<div align="center">
    <img src="https://github.com/user-attachments/assets/894fde7d-9f31-4802-b4ec-1b7d44c24e40" width="70%">
  </div>
  
  <div align="center">
    <img src="https://github.com/user-attachments/assets/942d3080-5a86-4328-bf92-f691665dba42" width="70%">
  </div>

  <div align="center">
    <img src="https://github.com/user-attachments/assets/86c9ee89-2da4-484b-bb32-1e8674b854a6" width="70%">
  </div>
