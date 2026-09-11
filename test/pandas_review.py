"""
glob : 정규표현식을 만족하는 목록들 가져올 때 사용하는 패키지 (라이브러리)
    ㄴ 정규표현식 : 특정 패턴을 만족하는 문자열 가져올 때 사용하는 문법
    ㄴ 여러 프로그래밍 언어에 지원
    > OBS_*.csv - * = 0번 이상 아무런 패턴이 매칭
    https://rpubs.com/qkdrk777777/511937
    [ㄱ-힣] : 한글
    [A-z] : 영어
    [ㄱ-힣A-z] : 한글과 영어 추출
    
특정 폴더에서 자료 가져오기


"""
import glob
file_dir = "C:/Users/user/Desktop/강의/2026.09.07/"

# 특정 폴더 안에 있는 csv 파일 목록 가져올 정규표현식
files = glob.glob(f"{file_dir}/*csv")

# glob.glob(정규표현식) : 표현식을 만족하는 자료만 추출
files = glob.glob(f"{file_dir}/O*.csv")
glob.glob(f"{file_dir}/**/O*.csv") # ** : 폴더 아무 이름
glob.glob(f"{file_dir}/**/**/O*.csv")

# glob.glob(recursive=True) 현재 폴더 안에 있는 모든 하위 폴더들 확인
# 재귀적으로 폴더를 추출
# 하위 폴더 모두 다 뒤져본 뒤에 O로 시작하고 csv로 끝나는 파일 목록 추출
import pandas as pd
files = glob.glob(f"{file_dir}/**/O*.csv",recursive=True)
len(files)

file = files[0]
df = pd.read_csv(file, encoding="cp949")
result = list()

for file in files:
    df = pd.read_csv(file, encoding="cp949")
    result.append(df)
    print(file)

tot_df = pd.concat(result) # 여러 파일을 병합
# 라벨로 추출하게 되면 중복 선택이 발생
tot_df.loc[4,:]
tot_df.iloc[4,:]
tot_df = tot_df.reset_index(drop=True)

# 159번에 해당하는 데이터 추출
# 특정 조건을 만족하는지 하지 않는지 True/False 반환
# 반환 받은 값을 행에 기입하면, 데이터가 추출
(tot_df.loc[:,"지점"] == 159).values
tot_df.loc[:,"지점"].isin([159]).values
cond = (tot_df.loc[:,"지점"] == 159).values
test = tot_df.iloc[cond,:]

# pandas에서 시간 관련 함수 사용해보기
tot_df.loc[:,"일시"] #dtype이 object이면 문자열을 의미

import datetime
datetime.datetime.now()

"""
pd.to_datetime(시간관련 컬럼) : 
    시간 형태(datetime)로 반환
"""
tot_df["일시"] = pd.to_datetime(tot_df.loc[:,"일시"]) 
    # 덮어씌워야지 반영
tot_df.loc[:,"일시"]
tot_df["일시"]
dir(tot_df["일시"].dt)
tot_df["일시"].dt.year
tot_df["일시"].dt.weekday
tot_df["일시"].dt.time
tot_df["일시"].dt.strftime("%y-%m-%d")
"""
%Y : 4자리 연도 / %y : 2자리 연도
%m : 2자리 월
%d : 2자리 일

%H : 시
%M : 분
%s : 초
""" 

# 8월 이후 데이터 추출하기
start_time = pd.to_datetime("2026-08-01")
cond1 = (tot_df["일시"]>start_time).values
extract_df = tot_df.iloc[cond1,:]

# 최소값
min(extract_df["일시"])
extract_df["일시"].min()

# 기초 통계량
extract_df.describe() 

# location_df 라는 이름으로 위치정보 파일 읽어오기
file_name = "C:/Users/user/Desktop/강의/2026.09.07/META_관측지점정보_20260901121943.csv"
location_df = pd.read_csv(file_name, encoding="cp949")
location_df
# location_df[특정컬럼].isnull 활용해서 종료일이 결측인 행들만 추출

cond1 = location_df["종료일"].isnull().values
#        location_df.loc[:,"종료일"].isnull()
location_df2 = location_df.iloc[cond1,:].reset_index(drop=True)

# 모든 지점의 건수가 1개가 맞는지 확인
location_df2["지점"].value_counts().max()

# tot_df에서 지점, 지점명, 일시, 기온만 추출
# location_df2에서 지점, 위도, 경도 추출
"""
tot_df.loc[:,[컬럼명1, 컬럼명2]]
tot_df.iloc[:,[컬럼위치1, 컬럼위치2]]
"""
tot_df.columns
tot_df2 = tot_df.loc[:,["지점","지점명","일시","기온(°C)"]]
tot_df.iloc[:,:4] # tot_df.iloc[:,:[0,1,2,3]] 

location_df2.columns
location_df3 = location_df2.loc[:,["지점","위도","경도"]]
location_df2.iloc[:,[0,6,7]]

"""
select 원하는 컬럼
from 테이블1 as t1 JOIN 테이블2 as t2
on t1.기준컬럼 = t2.기준컬럼
;
"""
# tot_df2,location_df3
# on 지점
"""
pd.merge(tot_df2,location_df3,how="조인방식",
         on = "결합하고 싶은 컬럼명")
pd.merge(tot_df2,location_df3,how="조인방식",
         on.x = 왼쪽 컬럼명, on.y = 오른쪽 컬럼명)
"""
concat_df = pd.merge(tot_df2,location_df3,how = "inner",on = "지점")
