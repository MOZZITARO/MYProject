# 영양 섭취 및 운동 추천 웹 애플리케이션 
### 프로젝트 개요

- 사용자가 섭취한 음식과 성별을 입력하면, 일일 권장 칼로리와 비교하여 섭취량을 분석하고, 그에 따른 운동 또는 추가 섭취 음식을 추천해주는 건강 관리 웹 애플리케이션입니다.

## <span id="3">📅 개발 일정</span>

### 프로젝트 개발 기간 : 2025.05.19 - 2025.05.21 ( 총 3 일 )


## <span id="3">📅 개발 스택</span>
<div align="center">
    <img src="https://github.com/user-attachments/assets/556eb84b-b62e-445a-aa0d-738af09b02fb" width="40%">


<div align="center">
    <img src="https://github.com/user-attachments/assets/d07436db-1db8-4334-965f-417715c6ed45" width="40%">
</div>

### 
<br>

# 🛠️ 주요기능
### 오늘 먹은 음식 입력

사용자가 입력한 음식 데이터를 바탕으로 성별과 활동 수준에 따른 일일 권장 칼로리와 비교 분석을 수행<br>
  <br>
  <div align="center">
    <img src="https://github.com/user-attachments/assets/f1b2063d-c246-4a4f-9b96-2af96cf5dcad" width="45%">
  </div>

   <div align="center">
    <img src="https://github.com/user-attachments/assets/b6c31c67-dfaf-400f-820f-afd8d2bb2470" width="45%">
  </div>


### 이력 저장

pymysql 라이브러리를 활용해 Flask와 연동하여 사용자 입력 데이터의 저장 및 조회 기능을 구현.<br>
    <br>
  <div align="center">
    <img src="https://github.com/user-attachments/assets/35abdc28-6343-4cd4-b112-4036b6251af2" width="45%">
  </div>


<br><br>

# 🛠️ 기술적 주안점


"개발 초기에는 모든 로직을 app.py한 파일에 작성했지만, 코드가 길어질수록 특정 함수를 찾기 어렵고 수정 시 실수가 발생하기 쉽다는 문제를 경험. 
이를 해결하기 위해 데이터베이스 관련 모든 기능을 db.py로 분리하여 관심사를 명확히 구분함.<br>
  <br>
  <div align="center">
    <img src="https://github.com/user-attachments/assets/dc85f87e-147d-4d3a-9cbe-4f39c7b59619" width="45%">
  </div>

