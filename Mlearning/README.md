# 학습 습관 기반 성적 예측 시스템
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


"개발 초기에는 모든 로직을 app.py한 파일에 작성했지만, 코드가 길어질수록 특정 함수를 찾기 어렵고 수정 시 실수가 발생하기 쉽다는 문제를 경험. 
이를 해결하기 위해 데이터베이스 관련 모든 기능을 db.py로 분리하여 관심사를 명확히 구분함.<br>
  <br> 특히 개발하면서 '사용자가 실제로 쓸 만한가?'를 고민. 그래서 음식 입력을 자연스럽게 쉼표로 구분하게 하고, 추천도 '운동하세요'가 아니라 '달리기 몇 시간'처럼 구체적으로 제시. 
  또한 매번 입력하는 것만으로는 의미가 없다고 생각해서 기록 저장과 이력 조회 기능을 추가하여 지속적인 건강 관리가 가능하도록 함."<br>
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
