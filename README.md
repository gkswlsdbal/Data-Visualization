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

## ColumnChart-Missing Value

- 파일을 불러올 때 열 정보를 unshowing column에 불러옵니다.
- Column : 기본적인 데이터만 표시
- Column Missing value : 기본적인 데이터 + 비어 있는 값 개수 표시
- Missing value : 비어 있는 값 개수만 표시
- show noting : 모든 열 표시 안함
- show everything : 모든열 표시

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
### 메인창
- 데이터 파일을 drag & drop으로 불러와서 각열에 대한 정보와 원하는 그래프로 표시합니다.

![캡처](https://user-images.githubusercontent.com/75991023/144609008-c9693007-2c28-448e-998d-299df7657d0c.JPG)
![캡처2](https://user-images.githubusercontent.com/75991023/144609634-45f32ace-2c4f-4d46-8309-8a0c3eca5f87.JPG)

### Column + Missing value

- 불러온 데이터 파일에 대한 기본적인 데이터와 비어 있는 값 개수를 표시합니다.

![캡처3](https://user-images.githubusercontent.com/75991023/144609980-5cde4e9d-d3ef-498d-b5bd-92705b105c70.JPG)

### 데이터 병합

- File Absorption :두 파일을 병합할때 사용합니다.

![캡처4](https://user-images.githubusercontent.com/75991023/144610632-838ddb15-ce75-4bf5-bf6b-15db6837067d.JPG)

-  Cell Absorption : 여러 테이블에서 열을 선택하고 병합

![캡처5](https://user-images.githubusercontent.com/75991023/144610789-e770bbf8-a34b-467a-93b2-bfbe05148f97.JPG)

### 데이터 전처리

- Clean Missing Data : 결측치 제거

![캡처6](https://user-images.githubusercontent.com/75991023/144611105-de41360f-fe54-4d06-ae41-295634581166.JPG)

- Remove Duplicate Rows : 중복 행 제거

![캡처2](https://user-images.githubusercontent.com/75991023/144611319-27961ff4-64b5-40f3-8a39-72266bcb7958.JPG)

- Clip Valies : 이상치 제거

![캡처3](https://user-images.githubusercontent.com/75991023/144611434-a19d592b-7dbd-47e9-bfa7-76f64b77fb5d.JPG)

- Smote : 표준화

![캡처4](https://user-images.githubusercontent.com/75991023/144611530-71ad5f1d-2a8a-4de5-9712-cda1e922e9a7.JPG)

- Normalize : 특성 정규화


![캡처5](https://user-images.githubusercontent.com/75991023/144611660-930de29d-032c-49bc-aa58-1562c1f8328b.JPG)


