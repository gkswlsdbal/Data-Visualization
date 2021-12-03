# 포트폴리오
## 데이터 시각화프로그램

자기소개를 위해 만들어본 포트폴리오입니다.

사용한 언어는 Python을 이용하였으며 , 툴은 PyCharm을 사용해 만들었습니다.

직접 실제로 사용해본다면 다양한 기능들을 볼 수 있습니다.

* * *
## Features

- 파이썬GUI을 이용한 데이터 작업 및 시각화프로그램
- 데이터 수정 및 저장 기능
- 데이터 병합 및 전처리 기능
- 데이터를 막대, 선, 원 등 다양한 그래프로 표현하는 시각화 기능


* * *

## 데이터 병합

- 열 병합 : 여러 테이블에서 열을 선택하고 병합하는 기능
- 파일 병합: 두 파일을 병합(교집합,합집합,left outer join, right outer join)


## 데이터 전처리
### Clean Missing Data

- 내가 원하는 값으로 대체
- 평균 값 처리
- 중앙 값 처리
- 최빈 값 처리
- 행 삭제
- 열 삭제

### Remove Duplicate Rows

- 체크 : 첫 번째 중복 행이 유지 되고 다른행은 삭제
- 체크 해제 : 마지막 중복행이 결과에 유지 되고 다른 행은 삭제

### Clip Values

Set of thresholds
- ClipPeaks : 상한을 지정
- ClipsubPeaks : 하한만 지정
- ClipPeakAndSubpeaks : 상한 및 하 한 경계 모두 지정

Threshold
- Constant : 상수
- percentile : 백분율

### Smote

- 데이터가 불균형할때 표준화시켜주는 역할
- 정상 데이터수를 기준으로 퍼센트 비율로 소수데이터가 합성된다.
- knn 알고리즘 이웃수 선택

### Normalize

- ZScore
- MinMax
- Robust
- Logistic
- LogNormal
- Tanh

* * *
## 실행화면
