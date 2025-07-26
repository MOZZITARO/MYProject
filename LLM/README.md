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
### 오늘 먹은 음식 입력

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


    "기존 방식에서는 매 요청마다 모델을 새로 로드하는 비효율적인 방식을 사용했으나, 전역 초기화 방식으로 변경하여 애플리케이션 시작 시 한 번만 모델을 메모리에 로드하도록 개선. 
    이를 통해 반복적인 모델 로딩을 제거하여 응답 시간을 대폭 단축. 
    추가로 Ollama 기반의 로컬 LLM을 선택하여 호출당 발생하는 운영 비용을 절약하고 네트워크 지연 시간을 줄여 응답 속도까지 향상.<br>
    
  <br> 초기에는 첫 번째 요청 시 전체 데이터셋을 일괄 로드하는 방식으로 인해 초기 응답 속도가 15-20초까지 지연되는 문제가 발생. 
  이를 해결하기 위해 필요한 첫 번째 데이터만 선택적으로 로드하도록 변경. "<br>

  외부 API의 신뢰성과 로컬 AI의 효율성을 전략적으로 결합 하이브리드 구조를 설계. 
  TMDB API가 실시간 영화 데이터와 포스터를 제공하면, Ollama LLM이 친근한 설명으로 변환하는 방식으로 결과적으로 데이터의 정확성(TMDB) + 설명의 지능성(Ollama) + 비용 효율성(로컬 처리)을 한번에 구현.
  <br>
  <div align="center">
    <img src="https://github.com/user-attachments/assets/50bae70e-ce67-4031-b283-22a0bb5a5278" width="70%">
  </div>

   <div align="center">
    <img src="https://github.com/user-attachments/assets/c3e621c3-e4ff-4683-8470-fe0d6a216c1b" width="70%">
  </div>

   <div align="center">
    <img src="https://github.com/user-attachments/assets/1e9ccecd-19f8-44b9-aa1b-87f6a3225028" width="70%">
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

