# 🐼 Pandas 상세 복습

## 📌 학습 개요

Python 데이터 분석에서 자주 사용하는 `Pandas` 라이브러리를 중심으로 데이터 생성, 조회, 선택, 정제, 중복 확인 등 기본 기능을 세부적으로 복습했습니다.

특히 `DataFrame`의 구조를 이해하고 `loc`, `iloc`을 활용하여 원하는 데이터를 선택하는 방법과 행·열의 개수를 확인하는 방법 등을 학습했습니다.

---

## 1. Pandas란?

`Pandas`는 Python에서 **표 형태의 데이터를 다루기 위한 데이터 분석 라이브러리**입니다.

Excel이나 데이터베이스의 테이블처럼 행과 열로 이루어진 데이터를 쉽게 처리할 수 있습니다.

```python
import pandas as pd
```

일반적으로 Pandas는 `pd`라는 이름으로 불러옵니다.

---

## 2. Series

`Series`는 Pandas에서 사용하는 **1차원 데이터 구조**입니다.

```python
import pandas as pd

data = pd.Series([10, 20, 30, 40])

print(data)
```

출력 예시

```text
0    10
1    20
2    30
3    40
dtype: int64
```

각 데이터에는 자동으로 `index`가 생성됩니다.

---

## 3. DataFrame

`DataFrame`은 **행과 열로 구성된 2차원 데이터 구조**입니다.

```python
data = {
    "name": ["Kim", "Lee", "Park"],
    "age": [20, 25, 30],
    "score": [90, 85, 95]
}

df = pd.DataFrame(data)

df
```

| index | name | age | score |
| ----- | ---- | --: | ----: |
| 0     | Kim  |  20 |    90 |
| 1     | Lee  |  25 |    85 |
| 2     | Park |  30 |    95 |

---

## 4. CSV 파일 불러오기

CSV 파일은 `read_csv()`를 사용하여 불러올 수 있습니다.

```python
df = pd.read_csv("data.csv")
```

파일 경로를 직접 지정할 수도 있습니다.

```python
df = pd.read_csv("C:/Users/user/Desktop/data.csv")
```

폴더 경로가 아니라 **CSV 파일 자체의 경로**를 입력해야 합니다.

---

## 5. 데이터 확인하기

### head()

데이터의 앞부분을 확인합니다.

```python
df.head()
```

기본적으로 앞에서부터 5개의 행을 보여줍니다.

```python
df.head(10)
```

위와 같이 작성하면 앞의 10개 행을 확인할 수 있습니다.

---

### tail()

데이터의 마지막 부분을 확인합니다.

```python
df.tail()
```

---

### info()

데이터의 전체적인 구조를 확인합니다.

```python
df.info()
```

확인할 수 있는 내용

* 행 개수
* 컬럼 이름
* NULL 여부
* 데이터 타입
* 메모리 사용량

---

### describe()

숫자형 데이터의 기초 통계 정보를 확인합니다.

```python
df.describe()
```

대표적으로 다음 정보를 확인할 수 있습니다.

* count
* mean
* std
* min
* 25%
* 50%
* 75%
* max

---

## 6. shape

`shape`을 사용하면 DataFrame의 **행과 열의 개수**를 확인할 수 있습니다.

```python
df.shape
```

예시

```text
(100, 5)
```

의미

```text
100개의 행
5개의 열
```

### 행의 개수

```python
df.shape[0]
```

### 열의 개수

```python
df.shape[1]
```

---

## 7. len()

`len()`을 사용해서도 행의 개수를 확인할 수 있습니다.

```python
len(df)
```

즉,

```python
len(df)
```

와

```python
df.shape[0]
```

은 모두 DataFrame의 **행 개수**를 확인할 때 사용할 수 있습니다.

---

## 8. 컬럼 확인하기

```python
df.columns
```

DataFrame이 가지고 있는 컬럼 이름을 확인할 수 있습니다.

---

## 9. 특정 컬럼 선택

하나의 컬럼을 선택할 때는 다음과 같이 사용할 수 있습니다.

```python
df["name"]
```

여러 개의 컬럼을 선택하려면 리스트 형태로 작성합니다.

```python
df[["name", "age"]]
```

---

## 10. loc

`loc`은 데이터의 **이름(Label)** 을 기준으로 데이터를 선택합니다.

```python
df.loc[0]
```

0번 인덱스의 행을 가져옵니다.

특정 행과 특정 컬럼을 함께 선택할 수도 있습니다.

```python
df.loc[0, "name"]
```

여러 개의 행과 열도 선택할 수 있습니다.

```python
df.loc[0:2, ["name", "age"]]
```

### loc 특징

```text
행과 열의 이름을 기준으로 선택
```

예를 들어

```python
df.loc[0, "name"]
```

은

```text
0번 인덱스의 name 컬럼
```

을 의미합니다.

---

## 11. iloc

`iloc`은 데이터의 **위치(Index Position)** 를 기준으로 데이터를 선택합니다.

```python
df.iloc[0]
```

첫 번째 행을 선택합니다.

```python
df.iloc[0, 1]
```

첫 번째 행의 두 번째 컬럼을 선택합니다.

### iloc 특징

```text
숫자로 데이터의 위치를 지정
```

Python의 인덱스는 `0`부터 시작합니다.

```text
0 → 첫 번째
1 → 두 번째
2 → 세 번째
```

---

## 12. loc과 iloc 비교

| 구분   | loc                 | iloc               |
| ---- | ------------------- | ------------------ |
| 기준   | 이름(Label)           | 위치(Index Position) |
| 행 선택 | 인덱스 이름              | 숫자 위치              |
| 열 선택 | 컬럼 이름               | 컬럼 위치              |
| 예시   | `df.loc[0, "name"]` | `df.iloc[0, 1]`    |

간단하게 기억하면

```text
loc  → 이름으로 찾기
iloc → 위치로 찾기
```

---

## 13. 조건을 이용한 데이터 조회

특정 조건을 만족하는 데이터만 선택할 수도 있습니다.

예를 들어 나이가 25 이상인 데이터를 조회하면

```python
df[df["age"] >= 25]
```

점수가 90 이상인 데이터를 조회하면

```python
df[df["score"] >= 90]
```

---

## 14. 여러 조건 사용하기

AND 조건은 `&`를 사용합니다.

```python
df[
    (df["age"] >= 20) &
    (df["score"] >= 90)
]
```

OR 조건은 `|`를 사용합니다.

```python
df[
    (df["age"] >= 30) |
    (df["score"] >= 90)
]
```

조건을 작성할 때 각각의 조건을 `()`로 묶어주는 것이 중요합니다.

---

## 15. 중복 데이터 확인

`duplicated()`를 사용하면 중복된 행을 확인할 수 있습니다.

```python
df.duplicated()
```

결과는 `True`, `False` 형태로 반환됩니다.

중복된 행의 개수만 확인하려면

```python
df.duplicated().sum()
```

을 사용할 수 있습니다.

```text
duplicated()
    ↓
중복 여부 확인

sum()
    ↓
True의 개수 계산
```

---

## 16. 중복 데이터 제거

중복된 데이터를 제거할 때는 `drop_duplicates()`를 사용합니다.

```python
df.drop_duplicates()
```

원본 DataFrame에 적용하려면

```python
df = df.drop_duplicates()
```

처럼 다시 저장할 수 있습니다.

---

## 17. 결측값 확인

결측값은 데이터가 비어 있는 상태를 의미합니다.

Pandas에서는 주로 `NaN`으로 표시됩니다.

```python
df.isnull()
```

컬럼별 결측값 개수를 확인하려면

```python
df.isnull().sum()
```

을 사용할 수 있습니다.

---

## 18. 결측값 제거

```python
df.dropna()
```

결측값이 존재하는 데이터를 제거할 수 있습니다.

---

## 19. 결측값 채우기

```python
df.fillna(0)
```

결측값을 특정 값으로 변경할 수 있습니다.

예를 들어 평균값으로 채우려면

```python
df["score"] = df["score"].fillna(df["score"].mean())
```

처럼 사용할 수 있습니다.

---

## 20. 데이터 타입 확인

```python
df.dtypes
```

각 컬럼의 데이터 타입을 확인할 수 있습니다.

대표적인 데이터 타입은 다음과 같습니다.

| 데이터 타입   | 의미           |
| -------- | ------------ |
| int64    | 정수           |
| float64  | 실수           |
| object   | 문자열 등        |
| bool     | True / False |
| datetime | 날짜 및 시간      |

---

## 21. 데이터 타입 변경

`astype()`을 사용하여 데이터 타입을 변경할 수 있습니다.

```python
df["age"] = df["age"].astype(int)
```

문자열로 변경하려면

```python
df["age"] = df["age"].astype(str)
```

---

## 22. 정렬하기

특정 컬럼을 기준으로 데이터를 정렬할 수 있습니다.

```python
df.sort_values("score")
```

기본값은 오름차순입니다.

내림차순으로 정렬하려면

```python
df.sort_values("score", ascending=False)
```

을 사용합니다.

---

## 23. 새로운 컬럼 추가

새로운 컬럼을 생성할 수도 있습니다.

```python
df["pass"] = df["score"] >= 60
```

예시

| name | score | pass  |
| ---- | ----: | ----- |
| Kim  |    90 | True  |
| Lee  |    50 | False |
| Park |    80 | True  |

---

## 24. 컬럼 삭제

```python
df.drop(columns=["pass"])
```

여러 개의 컬럼도 삭제할 수 있습니다.

```python
df.drop(columns=["age", "score"])
```

---

## 25. Pandas 데이터 처리 흐름

Pandas를 이용한 기본적인 데이터 처리 과정은 다음과 같이 정리할 수 있습니다.

```text
데이터 불러오기
        ↓
데이터 구조 확인
        ↓
필요한 행 / 열 선택
        ↓
결측값 및 중복값 확인
        ↓
데이터 정제
        ↓
조건에 맞는 데이터 추출
        ↓
데이터 분석 및 시각화
```

---

## 💡 학습하면서 정리한 핵심 포인트

### shape

```python
df.shape
```

```text
(행 개수, 열 개수)
```

---

### 행 개수

```python
len(df)
```

또는

```python
df.shape[0]
```

---

### 열 개수

```python
df.shape[1]
```

---

### 중복 행 개수

```python
df.duplicated().sum()
```

---

### loc

```python
df.loc[행 이름, 열 이름]
```

**Label 기준**

---

### iloc

```python
df.iloc[행 위치, 열 위치]
```

**숫자 위치 기준**

---

### 결측값 개수

```python
df.isnull().sum()
```

---

## 📚 이번 학습에서 느낀 점

Pandas는 단순히 데이터를 불러오는 라이브러리가 아니라, 데이터를 분석하기 전에 필요한 **조회, 선택, 정제, 가공 작업을 수행하는 핵심 도구**라는 것을 다시 확인했습니다.

특히 `loc`과 `iloc`, `shape`, `duplicated()`처럼 비슷해 보이는 기능들이 각각 어떤 기준으로 동작하는지 구분하는 것이 중요했습니다.

앞으로 실제 데이터를 분석할 때에도 다음 순서를 익숙하게 사용할 수 있도록 연습할 예정입니다.

```text
데이터 확인
→ 데이터 구조 파악
→ 필요한 데이터 선택
→ 데이터 정제
→ 분석
→ 시각화
```

---

## 🛠 사용 기술

* Python
* Pandas
* NumPy
* Jupyter Notebook
