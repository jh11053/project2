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

`DataFra
