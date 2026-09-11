"""
numpy : 고속 수치 연산을 위한 라이브러리
        python 내부에서 c로 만들어져서 python 기본 문법보다 빠름
        수학연산 관련 함수 다수 존재
    ㄴ자료형 : 문자형, 숫자형(int, float), 이미지형(uint8)(0~1, 0~255)
                ex) 빛의 3원색
    ㄴ객체구조 : 배열 (같은 타입의 길이가 같은 형태를 저장)
"""

# 배열 생성
# 1~9까지 배열 생성
import numpy as np
dir(np)
np.arange(1,10,1) # arange는 range와 다르게 간격을 소수로 기재 가능

# np.zeros, np.ones, np.full
# 2, 4 형태의 0값을 가지는 배열 생성하고 arr에 저장
arr = np.zeros((2,4))
arr = np.ones((2,4))
arr = np.full((2,4),3)

# np.full_like
# arr 활용해서 크기가 동일하고 값이 3인 배열 생성
np.full_like(arr,3)
np.zeros_like(arr)
np.ones_like(arr)

# 인덱싱, 슬라이싱
# 배열의 특징이 차원의 수가 무한(3차원, 4차원, ...)
# 사진(3차원) - (가로길이, 세로길이, 3)
# 동영상(4차원) - (총 사진의 수, 가로길이, 세로길이, 3-RGB)
#  ㄴ fps - frame per second
#  ㄴ 실시간 - 30fps 이상

img = np.zeros((256,512,3))
img.shape

# 가로의 픽셀 위치가 100~200, 세로의 위치가 100~200에 해당하는 값
# 시작:끝:간격
img[100:200,100:200,:]

# 가로의 픽셀 위치가 100~200, 세로의 위치가 100~200에 해당하고 파란색 값
img[100:200,100:200,2:]

# fps가 30일 때 2~3초 영상을 추출
video = np.zeros((600,256,512,3))
# 0:1초 -> 0:30
# 1~2초 -> 30:60
# 2~3초 -> 60:90
video[60:90,:,:,:]
video[60:90]

# 구조 변경(reshape, transpose)
# reshape : 배열의 모양 변경할 때 사용
arr = np.zeros((2,4))
arr
# 가로가 4줄 세로가 2줄로 변경
# arr.reshape(모양 - 튜플 형태로 기재)
arr.reshape((4,2))
# arr.T : 전치행렬 - 대각선을 기준으로 좌우 대칭한 배열을 반환
arr.T

# 배열 병합
# np.concatenate
# np.array([arr1,arr2,arr3,arr4]) : 배열 병합
img1 = np.zeros((256,256,3))
img2 = np.zeros((256,256,3))
img3 = np.zeros((256,256,3))
img4 = np.zeros((256,256,3))

my_list = [img1,img2,img3,img4]
arr = np.array(my_list)

# np.newaxis
img1.shape # 1,256,256,3
img1[np.newaxis,:,:,:] # 내가 추가하고 싶은 위치에 np.newaxis를 기재
img2[np.newaxis,:,:,:]
img3[np.newaxis,:,:,:]
img4[np.newaxis,:,:,:]
np.concatenate([
    img1[np.newaxis,:,:,:],
    img2[np.newaxis,:,:,:],
    img3[np.newaxis,:,:,:],
    img4[np.newaxis,:,:,:]
    ])

##########################################################################
"""
pandas : 표 형태 데이터를 다루기 용이하게 만들어진 라이브러리
        excel 형태 데이터 다루기에 용이
        excel 데이터 관리하는 데이터베이스인 RDBMS와 연결이 용이
        
리눅스 : Cron 통해서 데이터 주기적 기재 (9~10일 실습예정)

자료구조 :
    Series : 특정 컬럼 1개에 대해서 나타내는 자료구조
    DataFrame : 여러 컬럼 기준으로 나타내는 자료구조
        > 행렬 형태로 구성되어 있고, 각각의 열은 서로 다른 자료형태가 가능

인덱싱, 슬라이싱
    - iloc : index location을 활용해서 자료를 추출하는 방식
            위치 값으로 자료를 추출 df[행시작:끝:간격, 열시작:끝:간격]
    - loc : label location을 활용해서 자료를 추출하는 방식
            행의 이름, 열의 이름으로 자료를 추출
            df[행라벨, 열라벨]
"""
"""
조건을 부여한 자료 추출
   ㄴ 여러개 조건 부여 and(&)와 or(|) 사용이 가능
   ㄴ 조건1 and 조건2 : 앞의 조건(조건1)과 뒤의 조건(조건2) 
                      모두 만족하는 경우만 추출
   ㄴ 조건1 or 조건2 : 앞의 조건(조건1)과 뒤의 조건(조건2) 둘 중 하나만
                      만족하더라도 추출
"""
# df. iloc[조건1&조건2,:] 형태로 추출
import pandas as pd

data = {
        "state":["Ohio"]*3 + ["Nevada"]*3,
        "year":[2000,2001,2002,2001,2002,2003],
        "pop":[1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
        }
df = pd.DataFrame(data)
df
# Ohio 주에 2001년도 이상 자료만 추출
# 주와 관련된 컬럼 추출
df.loc[:,"state"]
df.iloc[:,0]

# Ohio인지 아닌지 True/False 반환
df.loc[:,"state"] == "Ohio"
df.iloc[:,0] == "Ohio"

# 연도와 관련된 컬럼 추출
df.loc[:,"year"]
df.iloc[:,1]

# 추출된 연도에서 2001년도 이상인지 아닌지 True/False 반환
df.loc[:,"year"] >= 2001
df.iloc[:,1] >= 2001

# 조건1, 조건2 가져오기
cond1 = df.loc[:,"state"] == "Ohio"
cond2 = df.loc[:,"year"] >= 2001
cond1 & cond2 # 조건1과 조건2 둘 다 만족하는 경우 True
(cond1 & cond2).values # 넘파이 값으로 변환
df.iloc[(cond1&cond2).values,:]

# isin : 특정 목록에 포함되는지 아닌지 True/False로 반환
data = {
        "state":["Ohio"]*3 + ["Nevada"]*3 + ["test"],
        "year":[2000,2001,2002,2001,2002,2003, 2005],
        "pop":[1.5, 1.7, 3.6, 2.4, 2.9, 3.2, 3.5]
        }
df = pd.DataFrame(data)
df
# df[특정 컬럼 선택].isin(목록 리스트) 기재
df.loc[:,"state"].isin(["Ohio","Nevada"])
df.loc[:,"state"].isin(["Ohio"])

# 
df.columns # 컬럼 목록 가져오기
# df.columns = [컬럼1,컬럼2,컬럼3] 형태로 컬럼명 변경 가능
df.columns = ["State","Year","Pop"]
df.columns
dir(df)
df = df.rename(columns={"State":"state","Year":"year","Pop":"pop"})
df

# 행 변경
list(df.index)
df.index = ["a","b","c","d","e","f","g"]
df.index
df

# 인덱스 숫자형태로 초기화 시키고 싶을 때
# reset_index 함수 활용
df.reset_index()
df

df2 = df.iloc[[2,5],:]
df2.loc[0,:]
df2.loc[2,:]
df2.reset_index(drop=True) # 기존의 인덱스 컬럼 필요없을 때 사용

filepath = "C:/Users/user/Desktop/강의/2026.09.07/META_관측지점정보_20260901121943.csv"
# read_csv : csv, tsv 확장자 읽을 때 활용
# read_excel : xlsx, xls 확장자 읽을 때 사용
# csv 파일은 ,를 기준으로 값을 구분
# tsv 파일은 tap을 기준으로 값을 구분
"""
encoding : 자료 저장 방식이 무엇인지 나타내는 기준
    ex) "cp949(windows 기본값)", "euc-kr", "utf-8(mac, linux"
"""
# 파일 읽었는데 안 읽히면 인코딩 확인
# 읽었는데 이상하게 읽힘 -> 구분자 확인
pd.read_csv(filepath, encoding = "cp949")

import os
os.chdir("C:/Users/user/Desktop/강의/2026.09.07")
os.listdir()
# os.listdir() : 현재 작업경로에 있는 파일 목록 보여줌
# glob : 특정 작업경로의 특정 파일 목록 가져올 수 있음
import glob
work_dir = "C:/Users/user/Desktop/강의/2026.09.07"
# 정규표현식 : 문자열을 추출할 때 사용하는 방법
# > OBS_*.csv : OBS_로 시작하고 .csv로 끝나며
# 그 사이에 여러개의 문자(*)가 랜덤하게 존재

glob.glob(f"{work_dir}/OBS_*.csv")
# glob.glob 함수는 특정 정규표현식을 만족하는 목록만 추출

# for문으로 파일 3개 읽어와서 화면에 출력하기
work_dir = "C:/Users/user/Desktop/강의/2026.09.07"
files = glob.glob(f"{work_dir}/OBS_*.csv")
my_list = []
for i in files:
    file = pd.read_csv(i,)
    my_list.append(file)    