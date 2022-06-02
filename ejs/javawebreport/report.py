import pandas as pd
import pymysql
import warnings
import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['figure.figsize']=[15,5]
warnings.filterwarnings(action='ignore')

# 데이터베이스 javaweb에 연결
pymysql.install_as_MySQLdb()
conn = pymysql.connect(host='localhost', user='root', password='0614', db='javaweb', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
sql = "select * from inputfile" # inputfile 테이블에 있는 데이터 sql로 받아옴
cur.execute(sql)
result = cur.fetchall()
df = pd.DataFrame(result)
df = df.rename(columns=df.iloc[0])
df = df.drop([df.index[0]])
df = df.rename(index = df.iloc[:,0])
data = df[['task1','task2','task3','task4','task5']]
print(data)

# core1의 task별 수행능력
core1_task = data.loc['core1', :] # core1 기준으로 task들을 모두 가져옴

core1_task_max_arr = [] # max 배열 생성
core1_task_min_arr = [] # min 배열 생성
core1_task_mean_arr = [] # mean 배열 생성

core1_task1_max = pd.to_numeric(core1_task["task1"]).max() # core1 기준 task1 최댓값
core1_task_max_arr.insert(0,core1_task1_max) # 배열에 0번째로 삽입
core1_task2_max = pd.to_numeric(core1_task["task2"]).max() # core1 기준 task2 최댓값
core1_task_max_arr.insert(1,core1_task2_max) # 배열에 1번째로 삽입
core1_task3_max = pd.to_numeric(core1_task["task3"]).max() # core1 기준 task3 최댓값
core1_task_max_arr.insert(2,core1_task3_max) # 배열에 2번째로 삽입
core1_task4_max = pd.to_numeric(core1_task["task4"]).max() # core1 기준 task4 최댓값
core1_task_max_arr.insert(3,core1_task4_max) # 배열에 3번째로 삽입
core1_task5_max = pd.to_numeric(core1_task["task5"]).max() # core1 기준 task5 최댓값
core1_task_max_arr.insert(4,core1_task5_max) # 배열에 4번째로 삽입

core1_task1_min = pd.to_numeric(core1_task["task1"]).min() # core1 기준 task1 최솟값
core1_task_min_arr.insert(0,core1_task1_min) # 배열에 0번째로 삽입
core1_task2_min = pd.to_numeric(core1_task["task2"]).min() # core1 기준 task2 최솟값
core1_task_min_arr.insert(1,core1_task2_min) # 배열에 1번째로 삽입
core1_task3_min = pd.to_numeric(core1_task["task3"]).min() # core1 기준 task3 최솟값
core1_task_min_arr.insert(2,core1_task3_min) # 배열에 2번째로 삽입
core1_task4_min = pd.to_numeric(core1_task["task4"]).min() # core1 기준 task4 최솟값
core1_task_min_arr.insert(3,core1_task4_min) # 배열에 3번째로 삽입
core1_task5_min = pd.to_numeric(core1_task["task5"]).min() # core1 기준 task5 최솟값
core1_task_min_arr.insert(4,core1_task5_min) # 배열에 4번째로 삽입

core1_task1_mean = pd.to_numeric(core1_task["task1"]).mean() # core1 기준 task1 평균값
core1_task_mean_arr.insert(0,core1_task1_mean) # 배열에 0번째로 삽입
core1_task2_mean = pd.to_numeric(core1_task["task2"]).mean() # core1 기준 task2 평균값
core1_task_mean_arr.insert(1,core1_task2_mean) # 배열에 1번째로 삽입
core1_task3_mean = pd.to_numeric(core1_task["task3"]).mean() # core1 기준 task3 평균값
core1_task_mean_arr.insert(2,core1_task3_mean) # 배열에 2번째로 삽입
core1_task4_mean = pd.to_numeric(core1_task["task4"]).mean() # core1 기준 task4 평균값
core1_task_mean_arr.insert(3,core1_task4_mean) # 배열에 3번째로 삽입
core1_task5_mean = pd.to_numeric(core1_task["task5"]).mean() # core1 기준 task5 평균값
core1_task_mean_arr.insert(4,core1_task5_mean) # 배열에 4번째로 삽입

core1_task.loc['avg'] = core1_task_mean_arr # mean행 추가
core1_task.loc['max'] = core1_task_max_arr # max행 추가
core1_task.loc['min'] = core1_task_min_arr # min행 추가

core1_task = core1_task.loc[['avg','max','min']] #mean행, max행, min행만 추출하여 저장
core1_task = core1_task.transpose() #그래프로 표현하기 위해 행과 열 변환
# print(core1_task)

core1_task = core1_task.astype(float)
core1_task.plot()
plt.title('20191412 강수정')
plt.suptitle('core1의 task별 수행능력', fontsize=15)
warnings.filterwarnings(action='ignore')
plt.savefig('core1_task.png')
plt.close()

# core2의 task별 수행능력
core2_task = data.loc['core2', :] # core2 기준으로 task들을 모두 가져옴

core2_task_max_arr = [] # core2 max 배열 생성
core2_task_min_arr = [] # core2 min 배열 생성
core2_task_mean_arr = [] # core2 mean 배열 생성

core2_task1_max = pd.to_numeric(core2_task["task1"]).max() # core2 기준 task1 최대값
core2_task_max_arr.insert(0,core2_task1_max) # 배열에 0번째로 삽입
core2_task2_max = pd.to_numeric(core2_task["task2"]).max() # core2 기준 task2 최대값
core2_task_max_arr.insert(1,core2_task2_max) # 배열에 1번째로 삽입
core2_task3_max = pd.to_numeric(core2_task["task3"]).max() # core2 기준 task3 최대값
core2_task_max_arr.insert(2,core2_task3_max) # 배열에 2번째로 삽입
core2_task4_max = pd.to_numeric(core2_task["task4"]).max() # core2 기준 task4 최대값
core2_task_max_arr.insert(3,core2_task4_max) # 배열에 3번째로 삽입
core2_task5_max = pd.to_numeric(core2_task["task5"]).max() # core2 기준 task5 최대값
core2_task_max_arr.insert(4,core2_task5_max) # 배열에 4번째로 삽입
# print(core2_task_max_arr)

core2_task1_min = pd.to_numeric(core2_task["task1"]).min() # core2 기준 task1 최솟값
core2_task_min_arr.insert(0,core2_task1_min) # 배열에 0번째로 삽입
core2_task2_min = pd.to_numeric(core2_task["task2"]).min() # core2 기준 task2 최솟값
core2_task_min_arr.insert(1,core2_task2_min) # 배열에 1번째로 삽입
core2_task3_min = pd.to_numeric(core2_task["task3"]).min() # core2 기준 task3 최솟값
core2_task_min_arr.insert(2,core2_task3_min) # 배열에 2번째로 삽입
core2_task4_min = pd.to_numeric(core2_task["task4"]).min() # core2 기준 task4 최솟값
core2_task_min_arr.insert(3,core2_task4_min) # 배열에 3번째로 삽입
core2_task5_min = pd.to_numeric(core2_task["task5"]).min() # core2 기준 task5 최솟값
core2_task_min_arr.insert(4,core2_task5_min) # 배열에 4번째로 삽입
# print(core2_task_min_arr)

core2_task1_mean = pd.to_numeric(core2_task["task1"]).mean() # core2 기준 task1 평균값
core2_task_mean_arr.insert(0,core2_task1_mean) # 배열에 0번째로 삽입
core2_task2_mean = pd.to_numeric(core2_task["task2"]).mean() # core2 기준 task2 평균값
core2_task_mean_arr.insert(1,core2_task2_mean) # 배열에 1번째로 삽입
core2_task3_mean = pd.to_numeric(core2_task["task3"]).mean() # core2 기준 task3 평균값
core2_task_mean_arr.insert(2,core2_task3_mean) # 배열에 2번째로 삽입
core2_task4_mean = pd.to_numeric(core2_task["task4"]).mean() # core2 기준 task4 평균값
core2_task_mean_arr.insert(3,core2_task4_mean) # 배열에 3번째로 삽입
core2_task5_mean = pd.to_numeric(core2_task["task5"]).mean() # core2 기준 task5 평균값
core2_task_mean_arr.insert(4,core2_task5_mean) # 배열에 4번째로 삽입
# print(core2_task_mean_arr)

core2_task.loc['avg'] = core2_task_mean_arr # mean행 추가
core2_task.loc['max'] = core2_task_max_arr # max행 추가
core2_task.loc['min'] = core2_task_min_arr # min행 추가
# print(core2_task)

core2_task = core2_task.loc[['avg','max','min']]
core2_task = core2_task.transpose()
# print(core2_task)

core2_task = core2_task.astype(float)
core2_task.plot()
plt.title('20191412 강수정')
plt.suptitle('core2의 task별 수행능력', fontsize=15)
plt.savefig('core2_task.png')
plt.close()
warnings.filterwarnings(action='ignore')

# core3의 task별 수행능력
core3_task = data.loc['core3', :] # core3 기준으로 task들을 모두 가져옴

core3_task_max_arr = [] # core3 max 배열 생성
core3_task_min_arr = [] # core3 min 배열 생성
core3_task_mean_arr = [] # core3 mean 배열 생성

core3_task1_max = pd.to_numeric(core3_task["task1"]).max() # core3 기준 task1 최댓값
core3_task_max_arr.insert(0,core3_task1_max) # 배열에 0번째로 삽입
core3_task2_max = pd.to_numeric(core3_task["task2"]).max() # core3 기준 task2 최댓값
core3_task_max_arr.insert(1,core3_task2_max) # 배열에 1번째로 삽입
core3_task3_max = pd.to_numeric(core3_task["task3"]).max() # core3 기준 task3 최댓값
core3_task_max_arr.insert(2,core3_task3_max) # 배열에 2번째로 삽입
core3_task4_max = pd.to_numeric(core3_task["task4"]).max() # core3 기준 task4 최댓값
core3_task_max_arr.insert(3,core3_task4_max) # 배열에 3번째로 삽입
core3_task5_max = pd.to_numeric(core3_task["task5"]).max() # core3 기준 task5 최댓값
core3_task_max_arr.insert(4,core3_task5_max) # 배열에 4번째로 삽입
# print(core3_task_max_arr)

core3_task1_min = pd.to_numeric(core3_task["task1"]).min() # core3 기준 task1 최솟값
core3_task_min_arr.insert(0,core3_task1_min) # 배열에 0번째로 삽입
core3_task2_min = pd.to_numeric(core3_task["task2"]).min() # core3 기준 task2 최솟값
core3_task_min_arr.insert(1,core3_task2_min) # 배열에 1번째로 삽입
core3_task3_min = pd.to_numeric(core3_task["task3"]).min() # core3 기준 task3 최솟값
core3_task_min_arr.insert(2,core3_task3_min) # 배열에 2번째로 삽입
core3_task4_min = pd.to_numeric(core3_task["task4"]).min() # core3 기준 task4 최솟값
core3_task_min_arr.insert(3,core3_task4_min) # 배열에 3번째로 삽입
core3_task5_min = pd.to_numeric(core3_task["task5"]).min() # core3 기준 task5 최솟값
core3_task_min_arr.insert(4,core3_task5_min) # 배열에 4번째로 삽입
# print(core3_task_min_arr)

core3_task1_mean = pd.to_numeric(core3_task["task1"]).mean() # core3 기준 task1 평균값
core3_task_mean_arr.insert(0,core3_task1_mean) # 배열에 0번째로 삽입
core3_task2_mean = pd.to_numeric(core3_task["task2"]).mean() # core3 기준 task2 평균값
core3_task_mean_arr.insert(1,core3_task2_mean) # 배열에 1번째로 삽입
core3_task3_mean = pd.to_numeric(core3_task["task3"]).mean() # core3 기준 task3 평균값
core3_task_mean_arr.insert(2,core3_task3_mean) # 배열에 2번째로 삽입
core3_task4_mean = pd.to_numeric(core3_task["task4"]).mean() # core3 기준 task4 평균값
core3_task_mean_arr.insert(3,core3_task4_mean) # 배열에 3번째로 삽입
core3_task5_mean = pd.to_numeric(core3_task["task5"]).mean() # core3 기준 task5 평균값
core3_task_mean_arr.insert(4,core3_task5_mean) # 배열에 4번째로 삽입
# print(core3_task_mean_arr)

core3_task.loc['avg'] = core3_task_mean_arr # mean행 추가
core3_task.loc['max'] = core3_task_max_arr # max행 추가
core3_task.loc['min'] = core3_task_min_arr # min행 추가
# print(core3_task)

core3_task = core3_task.loc[['avg','max','min']]
core3_task = core3_task.transpose()
# print(core3_task)

core3_task = core3_task.astype(float)
core3_task.plot()
plt.title('20191412 강수정')
plt.suptitle('core3의 task별 수행능력', fontsize=15)
plt.savefig('core3_task.png')
plt.close()
warnings.filterwarnings(action='ignore')

# core4의 task별 수행능력
core4_task = data.loc['core4', :] # core4 기준으로 task들을 모두 가져옴

core4_task_max_arr = [] # core4 max 배열 생성
core4_task_min_arr = [] # core4 min 배열 생성
core4_task_mean_arr = [] # core4 mean 배열 생성

core4_task1_max = pd.to_numeric(core4_task["task1"]).max() # core4 기준 task1 최댓값
core4_task_max_arr.insert(0,core4_task1_max) # 배열에 0번째로 삽입
core4_task2_max = pd.to_numeric(core4_task["task2"]).max() # core4 기준 task2 최댓값
core4_task_max_arr.insert(1,core4_task2_max) # 배열에 1번째로 삽입
core4_task3_max = pd.to_numeric(core4_task["task3"]).max() # core4 기준 task3 최댓값
core4_task_max_arr.insert(2,core4_task3_max) # 배열에 2번째로 삽입
core4_task4_max = pd.to_numeric(core4_task["task4"]).max() # core4 기준 task4 최댓값
core4_task_max_arr.insert(3,core4_task4_max) # 배열에 3번째로 삽입
core4_task5_max = pd.to_numeric(core4_task["task5"]).max() # core4 기준 task5 최댓값
core4_task_max_arr.insert(4,core4_task5_max) # 배열에 4번째로 삽입
# print(core4_task_max_arr)

core4_task1_min = pd.to_numeric(core4_task["task1"]).min() # core4 기준 task1 최솟값
core4_task_min_arr.insert(0,core4_task1_min) # 배열에 0번째로 삽입
core4_task2_min = pd.to_numeric(core4_task["task2"]).min() # core4 기준 task2 최솟값
core4_task_min_arr.insert(1,core4_task2_min) # 배열에 1번째로 삽입
core4_task3_min = pd.to_numeric(core4_task["task3"]).min() # core4 기준 task3 최솟값
core4_task_min_arr.insert(2,core4_task3_min) # 배열에 2번째로 삽입
core4_task4_min = pd.to_numeric(core4_task["task4"]).min() # core4 기준 task4 최솟값
core4_task_min_arr.insert(3,core4_task4_min) # 배열에 3번째로 삽입
core4_task5_min = pd.to_numeric(core4_task["task5"]).min() # core4 기준 task5 최솟값
core4_task_min_arr.insert(4,core4_task5_min) # 배열에 4번째로 삽입
# print(core4_task_min_arr)

core4_task1_mean = pd.to_numeric(core4_task["task1"]).mean() # core4 기준 task1 평균값
core4_task_mean_arr.insert(0,core4_task1_mean) # 배열에 0번째로 삽입
core4_task2_mean = pd.to_numeric(core4_task["task2"]).mean() # core4 기준 task2 평균값
core4_task_mean_arr.insert(1,core4_task2_mean) # 배열에 1번째로 삽입
core4_task3_mean = pd.to_numeric(core4_task["task3"]).mean() # core4 기준 task3 평균값
core4_task_mean_arr.insert(2,core4_task3_mean) # 배열에 2번째로 삽입
core4_task4_mean = pd.to_numeric(core4_task["task4"]).mean() # core4 기준 task4 평균값
core4_task_mean_arr.insert(3,core4_task4_mean) # 배열에 3번째로 삽입
core4_task5_mean = pd.to_numeric(core4_task["task5"]).mean() # core4 기준 task5 평균값
core4_task_mean_arr.insert(4,core4_task5_mean) # 배열에 4번째로 삽입
# print(core4_task_mean_arr)

core4_task.loc['avg'] = core4_task_mean_arr # mean행 추가
core4_task.loc['max'] = core4_task_max_arr # max행 추가
core4_task.loc['min'] = core4_task_min_arr # min행 추가
# print(core4_task)

core4_task = core4_task.loc[['avg','max','min']]
core4_task = core4_task.transpose()
# print(core4_task)

core4_task = core4_task.astype(float)
core4_task.plot()
plt.title('20191412 강수정')
plt.suptitle('core4의 task별 수행능력', fontsize=15)
plt.savefig('core4_task.png')
plt.close()
warnings.filterwarnings(action='ignore')

# core5의 task별 수행능력
core5_task = data.loc['core5', :] # core5 기준으로 task들을 모두 가져옴

core5_task_max_arr = [] # core5 max 배열 생성
core5_task_min_arr = [] # core5 min 배열 생성
core5_task_mean_arr = [] # core5 mean 배열 생성

core5_task1_max = pd.to_numeric(core5_task["task1"]).max() # core5 기준 task1 최댓값
core5_task_max_arr.insert(0,core5_task1_max) # 배열에 0번째로 삽입
core5_task2_max = pd.to_numeric(core5_task["task2"]).max() # core5 기준 task2 최댓값
core5_task_max_arr.insert(1,core5_task2_max) # 배열에 1번째로 삽입
core5_task3_max = pd.to_numeric(core5_task["task3"]).max() # core5 기준 task3 최댓값
core5_task_max_arr.insert(2,core5_task3_max) # 배열에 2번째로 삽입
core5_task4_max = pd.to_numeric(core5_task["task4"]).max() # core5 기준 task4 최댓값
core5_task_max_arr.insert(3,core5_task4_max) # 배열에 3번째로 삽입
core5_task5_max = pd.to_numeric(core5_task["task5"]).max() # core5 기준 task5 최댓값
core5_task_max_arr.insert(4,core5_task5_max) # 배열에 4번째로 삽입
# print(core5_task_max_arr)

core5_task1_min = pd.to_numeric(core5_task["task1"]).min() # core5 기준 task1 최솟값
core5_task_min_arr.insert(0,core5_task1_min) # 배열에 0번째로 삽입
core5_task2_min = pd.to_numeric(core5_task["task2"]).min() # core5 기준 task2 최솟값
core5_task_min_arr.insert(1,core5_task2_min) # 배열에 1번째로 삽입
core5_task3_min = pd.to_numeric(core5_task["task3"]).min() # core5 기준 task3 최솟값
core5_task_min_arr.insert(2,core5_task3_min) # 배열에 2번째로 삽입
core5_task4_min = pd.to_numeric(core5_task["task4"]).min() # core5 기준 task4 최솟값
core5_task_min_arr.insert(3,core5_task4_min) # 배열에 3번째로 삽입
core5_task5_min = pd.to_numeric(core5_task["task5"]).min() # core5 기준 task5 최솟값
core5_task_min_arr.insert(4,core5_task5_min) # 배열에 4번째로 삽입
# print(core5_task_min_arr)

core5_task1_mean = pd.to_numeric(core5_task["task1"]).mean() # core5 기준 task1 평균값
core5_task_mean_arr.insert(0,core5_task1_mean) # 배열에 0번째로 삽입
core5_task2_mean = pd.to_numeric(core5_task["task2"]).mean() # core5 기준 task2 평균값
core5_task_mean_arr.insert(1,core5_task2_mean) # 배열에 1번째로 삽입
core5_task3_mean = pd.to_numeric(core5_task["task3"]).mean() # core5 기준 task3 평균값
core5_task_mean_arr.insert(2,core5_task3_mean) # 배열에 2번째로 삽입
core5_task4_mean = pd.to_numeric(core5_task["task4"]).mean() # core5 기준 task4 평균값
core5_task_mean_arr.insert(3,core5_task4_mean) # 배열에 3번째로 삽입
core5_task5_mean = pd.to_numeric(core5_task["task5"]).mean() # core5 기준 task5 평균값
core5_task_mean_arr.insert(4,core5_task5_mean) # 배열에 4번째로 삽입
# print(core5_task_mean_arr)

core5_task.loc['avg'] = core5_task_mean_arr # mean행 추가
core5_task.loc['max'] = core5_task_max_arr # max행 추가
core5_task.loc['min'] = core5_task_min_arr # min행 추가
# print(core5_task)

core5_task = core5_task.loc[['avg','max','min']]
core5_task = core5_task.transpose()
# print(core5_task)

core5_task = core5_task.astype(float)
core5_task.plot()
plt.title('20191412 강수정')
plt.suptitle('core5의 task별 수행능력', fontsize=15)
plt.savefig('core5_task.png')
plt.close()
warnings.filterwarnings(action='ignore')

# task1의 core별 수행능력

# 최댓값, 최솟값, 평균값을 행으로 추가하는 방식으로 진행하기 위해 재정렬을 진행하는 과정
task1_core = data.loc[:,'task1'] # task1 기준으로 core들을 모두 가져옴
# print(task1_core)

task1_core1 = pd.to_numeric(task1_core["core1"]) # task1 기준 core1 나열(to_numeric함수 사용하여 자료형 int로 변경 > 최솟값과 최댓값을 찾아내지 못하는 문제 발생 > 자료형 문제였음)
task1_core1_rename = task1_core1.rename(index={"core1":"task1"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task1으로 통일

task1_core2 = pd.to_numeric(task1_core["core2"]) # task1 기준 core2 나열
task1_core2_rename = task1_core2.rename(index={"core2":"task1"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task1으로 통일

task1_core3 = pd.to_numeric(task1_core["core3"]) # task1 기준 core3 나열
task1_core3_rename = task1_core3.rename(index={"core3":"task1"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task1으로 통일

task1_core4 = pd.to_numeric(task1_core["core4"]) # task1 기준 core4 나열
task1_core4_rename = task1_core4.rename(index={"core4":"task1"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task1으로 통일

task1_core5 = pd.to_numeric(task1_core["core5"]) # task1 기준 core5 나열
task1_core5_rename = task1_core5.rename(index={"core5":"task1"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task1으로 통일

task1_core_realignment = pd.concat([task1_core1_rename,task1_core2_rename,task1_core3_rename,task1_core4_rename,task1_core5_rename],axis=1,keys=['core1','core2','core3','core4','core5'])
# print(task1_core_realignment) # task1의 core별로 재정렬 진행 완료

task1_core_max_arr = [] # max 배열 생성
task1_core_min_arr = [] # min 배열 생성
task1_core_mean_arr = [] # mean 배열 생성

task1_core1_max = task1_core_realignment["core1"].max() # task1 기준 core1 최댓값
task1_core_max_arr.insert(0,task1_core1_max) # 배열에 0번째로 삽입
task1_core2_max = task1_core_realignment["core2"].max() # task1 기준 core2 최댓값
task1_core_max_arr.insert(1,task1_core2_max) # 배열에 1번째로 삽입
task1_core3_max = task1_core_realignment["core3"].max() # task1 기준 core3 최댓값
task1_core_max_arr.insert(2,task1_core3_max) # 배열에 2번째로 삽입
task1_core4_max = task1_core_realignment["core4"].max() # task1 기준 core4 최댓값
task1_core_max_arr.insert(3,task1_core4_max) # 배열에 3번째로 삽입
task1_core5_max = task1_core_realignment["core5"].max() # task1 기준 core5 최댓값
task1_core_max_arr.insert(4,task1_core5_max) # 배열에 4번째로 삽입
# print(task1_core_max_arr)

task1_core1_min = task1_core_realignment["core1"].min() # task1 기준 core1 최솟값
task1_core_min_arr.insert(0,task1_core1_min) # 배열에 0번째로 삽입
task1_core2_min = task1_core_realignment["core2"].min() # task1 기준 core2 최솟값
task1_core_min_arr.insert(1,task1_core2_min) # 배열에 1번째로 삽입
task1_core3_min = task1_core_realignment["core3"].min() # task1 기준 core3 최솟값
task1_core_min_arr.insert(2,task1_core3_min) # 배열에 2번째로 삽입
task1_core4_min = task1_core_realignment["core4"].min() # task1 기준 core4 최솟값
task1_core_min_arr.insert(3,task1_core4_min) # 배열에 3번째로 삽입
task1_core5_min = task1_core_realignment["core5"].min() # task1 기준 core5 최솟값
task1_core_min_arr.insert(4,task1_core5_min) # 배열에 4번째로 삽입
# print(task1_core_min_arr)

task1_core1_mean = task1_core_realignment["core1"].mean() # task1 기준 core1 평균값
task1_core_mean_arr.insert(0,task1_core1_mean) # 배열에 0번째로 삽입
task1_core2_mean = task1_core_realignment["core2"].mean() # task1 기준 core2 평균값
task1_core_mean_arr.insert(1,task1_core2_mean) # 배열에 1번째로 삽입
task1_core3_mean = task1_core_realignment["core3"].mean() # task1 기준 core3 평균값
task1_core_mean_arr.insert(2,task1_core3_mean) # 배열에 2번째로 삽입
task1_core4_mean = task1_core_realignment["core4"].mean() # task1 기준 core4 평균값
task1_core_mean_arr.insert(3,task1_core4_mean) # 배열에 3번째로 삽입
task1_core5_mean = task1_core_realignment["core5"].mean() # task1 기준 core5 평균값
task1_core_mean_arr.insert(4,task1_core5_mean) # 배열에 4번째로 삽입
# print(task1_core_mean_arr)

task1_core_realignment.loc['avg'] = task1_core_mean_arr # mean행 추가
task1_core_realignment.loc['max'] = task1_core_max_arr # max행 추가
task1_core_realignment.loc['min'] = task1_core_min_arr # min행 추가
# print(task1_core_realignment)

task1_core_realignment = task1_core_realignment.loc[['avg','max','min']]
task1_core_realignment = task1_core_realignment.transpose()
# print(task1_core_realignment)

task1_core_realignment = task1_core_realignment.astype(float)
task1_core_realignment.plot()
plt.title('20191412 강수정')
plt.suptitle('task1의 core별 수행능력', fontsize=15)
plt.savefig('task1_core.png')
plt.close()
warnings.filterwarnings(action='ignore')

# task2의 core별 수행능력

# 최댓값, 최솟값, 평균값을 행으로 추가하는 방식으로 진행하기 위해 재정렬을 진행하는 과정
task2_core = data.loc[:,'task2'] # task2 기준으로 core들을 모두 가져옴
# print(task2_core)

task2_core1 = pd.to_numeric(task2_core["core1"]) # task2 기준 core1 나열(to_numeric함수 사용하여 자료형 int로 변경 > 최솟값과 최댓값을 찾아내지 못하는 문제 발생 > 자료형 문제였음)
task2_core1_rename = task2_core1.rename(index={"core1":"task2"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task2으로 통일
task2_core2 = pd.to_numeric(task2_core["core2"]) # task2 기준 core2 나열
task2_core2_rename = task2_core2.rename(index={"core2":"task2"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task2으로 통일
task2_core3 = pd.to_numeric(task2_core["core3"]) # task2 기준 core3 나열
task2_core3_rename = task2_core3.rename(index={"core3":"task2"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task2으로 통일
task2_core4 = pd.to_numeric(task2_core["core4"]) # task2 기준 core4 나열
task2_core4_rename = task2_core4.rename(index={"core4":"task2"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task2으로 통일
task2_core5 = pd.to_numeric(task2_core["core5"]) # task2 기준 core5 나열
task2_core5_rename = task2_core5.rename(index={"core5":"task2"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task2으로 통일

task2_core_realignment = pd.concat([task2_core1_rename,task2_core2_rename,task2_core3_rename,task2_core4_rename,task2_core5_rename],axis=1,keys=['core1','core2','core3','core4','core5'])
# print(task2_core_realignment) # task2의 core별로 재정렬 진행 완료

task2_core_max_arr = [] # max 배열 생성
task2_core_min_arr = [] # min 배열 생성
task2_core_mean_arr = [] # mean 배열 생성

task2_core1_max = task2_core_realignment["core1"].max() # task2 기준 core1 최댓값
task2_core_max_arr.insert(0,task2_core1_max) # 배열에 0번째로 삽입
task2_core2_max = task2_core_realignment["core2"].max() # task2 기준 core2 최댓값
task2_core_max_arr.insert(1,task2_core2_max) # 배열에 1번째로 삽입
task2_core3_max = task2_core_realignment["core3"].max() # task2 기준 core3 최댓값
task2_core_max_arr.insert(2,task2_core3_max) # 배열에 2번째로 삽입
task2_core4_max = task2_core_realignment["core4"].max() # task2 기준 core4 최댓값
task2_core_max_arr.insert(3,task2_core4_max) # 배열에 3번째로 삽입
task2_core5_max = task2_core_realignment["core5"].max() # task2 기준 core5 최댓값
task2_core_max_arr.insert(4,task2_core5_max) # 배열에 4번째로 삽입
# print(task2_core_max_arr)

task2_core1_min = task2_core_realignment["core1"].min() # task2 기준 core1 최솟값
task2_core_min_arr.insert(0,task2_core1_min) # 배열에 0번째로 삽입
task2_core2_min = task2_core_realignment["core2"].min() # task2 기준 core2 최솟값
task2_core_min_arr.insert(1,task2_core2_min) # 배열에 1번째로 삽입
task2_core3_min = task2_core_realignment["core3"].min() # task2 기준 core3 최솟값
task2_core_min_arr.insert(2,task2_core3_min) # 배열에 2번째로 삽입
task2_core4_min = task2_core_realignment["core4"].min() # task2 기준 core4 최솟값
task2_core_min_arr.insert(3,task2_core4_min) # 배열에 3번째로 삽입
task2_core5_min = task2_core_realignment["core5"].min() # task2 기준 core5 최솟값
task2_core_min_arr.insert(4,task2_core5_min) # 배열에 4번째로 삽입
# print(task2_core_min_arr)

task2_core1_mean = task2_core_realignment["core1"].mean() # task2 기준 core1 평균값
task2_core_mean_arr.insert(0,task2_core1_mean) # 배열에 0번째로 삽입
task2_core2_mean = task2_core_realignment["core2"].mean() # task2 기준 core2 평균값
task2_core_mean_arr.insert(1,task2_core2_mean) # 배열에 1번째로 삽입
task2_core3_mean = task2_core_realignment["core3"].mean() # task2 기준 core3 평균값
task2_core_mean_arr.insert(2,task2_core3_mean) # 배열에 2번째로 삽입
task2_core4_mean = task2_core_realignment["core4"].mean() # task2 기준 core4 평균값
task2_core_mean_arr.insert(3,task2_core4_mean) # 배열에 3번째로 삽입
task2_core5_mean = task2_core_realignment["core5"].mean() # task2 기준 core5 평균값
task2_core_mean_arr.insert(4,task2_core5_mean) # 배열에 4번째로 삽입
# print(task2_core_mean_arr)

task2_core_realignment.loc['avg'] = task2_core_mean_arr # mean행 추가
task2_core_realignment.loc['max'] = task2_core_max_arr # max행 추가
task2_core_realignment.loc['min'] = task2_core_min_arr # min행 추가
# print(task2_core_realignment)

task2_core_realignment = task2_core_realignment.loc[['avg','max','min']]
task2_core_realignment = task2_core_realignment.transpose()
# print(task2_core_realignment)

task2_core_realignment = task2_core_realignment.astype(float)
task2_core_realignment.plot()
plt.title('20191412 강수정')
plt.suptitle('task2의 core별 수행능력', fontsize=15)
plt.savefig('task2_core.png')
plt.close()
warnings.filterwarnings(action='ignore')

# task3의 core별 수행능력

# 최댓값, 최솟값, 평균값을 행으로 추가하는 방식으로 진행하기 위해 재정렬을 진행하는 과정
task3_core = data.loc[:,'task3'] # task3 기준으로 core들을 모두 가져옴
# print(task3_core)

task3_core1 = pd.to_numeric(task3_core["core1"]) # task3 기준 core1 나열(to_numeric함수 사용하여 자료형 int로 변경 > 최솟값과 최댓값을 찾아내지 못하는 문제 발생 > 자료형 문제였음)
task3_core1_rename = task3_core1.rename(index={"core1":"task3"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task3으로 통일
task3_core2 = pd.to_numeric(task3_core["core2"]) # task3 기준 core2 나열
task3_core2_rename = task3_core2.rename(index={"core2":"task3"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task3으로 통일
task3_core3 = pd.to_numeric(task3_core["core3"]) # task3 기준 core3 나열
task3_core3_rename = task3_core3.rename(index={"core3":"task3"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task3으로 통일
task3_core4 = pd.to_numeric(task3_core["core4"]) # task3 기준 core4 나열
task3_core4_rename = task3_core4.rename(index={"core4":"task3"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task3으로 통일
task3_core5 = pd.to_numeric(task3_core["core5"]) # task3 기준 core5 나열
task3_core5_rename = task3_core5.rename(index={"core5":"task3"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task3으로 통일

task3_core_realignment = pd.concat([task3_core1_rename,task3_core2_rename,task3_core3_rename,task3_core4_rename,task3_core5_rename],axis=1,keys=['core1','core2','core3','core4','core5'])
# print(task3_core_realignment) # task3의 core별로 재정렬 진행 완료

task3_core_max_arr = [] # max 배열 생성
task3_core_min_arr = [] # min 배열 생성
task3_core_mean_arr = [] # mean 배열 생성

task3_core1_max = task3_core_realignment["core1"].max() # task3 기준 core1 최댓값
task3_core_max_arr.insert(0,task3_core1_max) # 배열에 0번째로 삽입
task3_core2_max = task3_core_realignment["core2"].max() # task3 기준 core2 최댓값
task3_core_max_arr.insert(1,task3_core2_max) # 배열에 1번째로 삽입
task3_core3_max = task3_core_realignment["core3"].max() # task3 기준 core3 최댓값
task3_core_max_arr.insert(2,task3_core3_max) # 배열에 2번째로 삽입
task3_core4_max = task3_core_realignment["core4"].max() # task3 기준 core4 최댓값
task3_core_max_arr.insert(3,task3_core4_max) # 배열에 3번째로 삽입
task3_core5_max = task3_core_realignment["core5"].max() # task3 기준 core5 최댓값
task3_core_max_arr.insert(4,task3_core5_max) # 배열에 4번째로 삽입
# print(task3_core_max_arr)

task3_core1_min = task3_core_realignment["core1"].min() # task3 기준 core1 최솟값
task3_core_min_arr.insert(0,task3_core1_min) # 배열에 0번째로 삽입
task3_core2_min = task3_core_realignment["core2"].min() # task3 기준 core2 최솟값
task3_core_min_arr.insert(1,task3_core2_min) # 배열에 1번째로 삽입
task3_core3_min = task3_core_realignment["core3"].min() # task3 기준 core3 최솟값
task3_core_min_arr.insert(2,task3_core3_min) # 배열에 2번째로 삽입
task3_core4_min = task3_core_realignment["core4"].min() # task3 기준 core4 최솟값
task3_core_min_arr.insert(3,task3_core4_min) # 배열에 3번째로 삽입
task3_core5_min = task3_core_realignment["core5"].min() # task3 기준 core5 최솟값
task3_core_min_arr.insert(4,task3_core5_min) # 배열에 4번째로 삽입
# print(task3_core_min_arr)

task3_core1_mean = task3_core_realignment["core1"].mean() # task3 기준 core1 평균값
task3_core_mean_arr.insert(0,task3_core1_mean) # 배열에 0번째로 삽입
task3_core2_mean = task3_core_realignment["core2"].mean() # task3 기준 core2 평균값
task3_core_mean_arr.insert(1,task3_core2_mean) # 배열에 1번째로 삽입
task3_core3_mean = task3_core_realignment["core3"].mean() # task3 기준 core3 평균값
task3_core_mean_arr.insert(2,task3_core3_mean) # 배열에 2번째로 삽입
task3_core4_mean = task3_core_realignment["core4"].mean() # task3 기준 core4 평균값
task3_core_mean_arr.insert(3,task3_core4_mean) # 배열에 3번째로 삽입
task3_core5_mean = task3_core_realignment["core5"].mean() # task3 기준 core5 평균값
task3_core_mean_arr.insert(4,task3_core5_mean) # 배열에 4번째로 삽입
# print(task3_core_mean_arr)

task3_core_realignment.loc['avg'] = task3_core_mean_arr # mean행 추가
task3_core_realignment.loc['max'] = task3_core_max_arr # max행 추가
task3_core_realignment.loc['min'] = task3_core_min_arr # min행 추가
# print(task3_core_realignment)

task3_core_realignment = task3_core_realignment.loc[['avg','max','min']]
task3_core_realignment = task3_core_realignment.transpose()
# print(task3_core_realignment)

task3_core_realignment = task3_core_realignment.astype(float)
task3_core_realignment.plot()
plt.title('20191412 강수정')
plt.suptitle('task3의 core별 수행능력', fontsize=15)
plt.savefig('task3_core.png')
plt.close()
warnings.filterwarnings(action='ignore')

# task4의 core별 수행능력

# 최댓값, 최솟값, 평균값을 행으로 추가하는 방식으로 진행하기 위해 재정렬을 진행하는 과정
task4_core = data.loc[:,'task4'] # task4 기준으로 core들을 모두 가져옴
# print(task4_core)

task4_core1 = pd.to_numeric(task4_core["core1"]) # task4 기준 core1 나열(to_numeric함수 사용하여 자료형 int로 변경 > 최솟값과 최댓값을 찾아내지 못하는 문제 발생 > 자료형 문제였음)
task4_core1_rename = task4_core1.rename(index={"core1":"task4"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task4으로 통일
task4_core2 = pd.to_numeric(task4_core["core2"]) # task4 기준 core2 나열
task4_core2_rename = task4_core2.rename(index={"core2":"task4"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task4으로 통일
task4_core3 = pd.to_numeric(task4_core["core3"]) # task4 기준 core3 나열
task4_core3_rename = task4_core3.rename(index={"core3":"task4"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task4으로 통일
task4_core4 = pd.to_numeric(task4_core["core4"]) # task4 기준 core4 나열
task4_core4_rename = task4_core4.rename(index={"core4":"task4"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task4으로 통일
task4_core5 = pd.to_numeric(task4_core["core5"]) # task4 기준 core5 나열
task4_core5_rename = task4_core5.rename(index={"core5":"task4"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task4으로 통일

task4_core_realignment = pd.concat([task4_core1_rename,task4_core2_rename,task4_core3_rename,task4_core4_rename,task4_core5_rename],axis=1,keys=['core1','core2','core3','core4','core5'])
# print(task4_core_realignment) # task4의 core별로 재정렬 진행 완료

task4_core_max_arr = [] # max 배열 생성
task4_core_min_arr = [] # min 배열 생성
task4_core_mean_arr = [] # mean 배열 생성

task4_core1_max = task4_core_realignment["core1"].max() # task4 기준 core1 최댓값
task4_core_max_arr.insert(0,task4_core1_max) # 배열에 0번째로 삽입
task4_core2_max = task4_core_realignment["core2"].max() # task4 기준 core2 최댓값
task4_core_max_arr.insert(1,task4_core2_max) # 배열에 1번째로 삽입
task4_core3_max = task4_core_realignment["core3"].max() # task4 기준 core3 최댓값
task4_core_max_arr.insert(2,task4_core3_max) # 배열에 2번째로 삽입
task4_core4_max = task4_core_realignment["core4"].max() # task4 기준 core4 최댓값
task4_core_max_arr.insert(3,task4_core4_max) # 배열에 3번째로 삽입
task4_core5_max = task4_core_realignment["core5"].max() # task4 기준 core5 최댓값
task4_core_max_arr.insert(4,task4_core5_max) # 배열에 4번째로 삽입
# print(task4_core_max_arr)

task4_core1_min = task4_core_realignment["core1"].min() # task4 기준 core1 최솟값
task4_core_min_arr.insert(0,task4_core1_min) # 배열에 0번째로 삽입
task4_core2_min = task4_core_realignment["core2"].min() # task4 기준 core2 최솟값
task4_core_min_arr.insert(1,task4_core2_min) # 배열에 1번째로 삽입
task4_core3_min = task4_core_realignment["core3"].min() # task4 기준 core3 최솟값
task4_core_min_arr.insert(2,task4_core3_min) # 배열에 2번째로 삽입
task4_core4_min = task4_core_realignment["core4"].min() # task4 기준 core4 최솟값
task4_core_min_arr.insert(3,task4_core4_min) # 배열에 3번째로 삽입
task4_core5_min = task4_core_realignment["core5"].min() # task4 기준 core5 최솟값
task4_core_min_arr.insert(4,task4_core5_min) # 배열에 4번째로 삽입
# print(task4_core_min_arr)

task4_core1_mean = task4_core_realignment["core1"].mean() # task4 기준 core1 평균값
task4_core_mean_arr.insert(0,task4_core1_mean) # 배열에 0번째로 삽입
task4_core2_mean = task4_core_realignment["core2"].mean() # task4 기준 core2 평균값
task4_core_mean_arr.insert(1,task4_core2_mean) # 배열에 1번째로 삽입
task4_core3_mean = task4_core_realignment["core3"].mean() # task4 기준 core3 평균값
task4_core_mean_arr.insert(2,task4_core3_mean) # 배열에 2번째로 삽입
task4_core4_mean = task4_core_realignment["core4"].mean() # task4 기준 core4 평균값
task4_core_mean_arr.insert(3,task4_core4_mean) # 배열에 3번째로 삽입
task4_core5_mean = task4_core_realignment["core5"].mean() # task4 기준 core5 평균값
task4_core_mean_arr.insert(4,task4_core5_mean) # 배열에 4번째로 삽입
# print(task4_core_mean_arr)

task4_core_realignment.loc['avg'] = task4_core_mean_arr # mean행 추가
task4_core_realignment.loc['max'] = task4_core_max_arr # max행 추가
task4_core_realignment.loc['min'] = task4_core_min_arr # min행 추가
# print(task4_core_realignment)

task4_core_realignment = task4_core_realignment.loc[['avg','max','min']]
task4_core_realignment = task4_core_realignment.transpose()
# print(task4_core_realignment)

task4_core_realignment = task4_core_realignment.astype(float)
task4_core_realignment.plot()
plt.title('20191412 강수정')
plt.suptitle('task4의 core별 수행능력', fontsize=15)
plt.savefig('task4_core.png')
plt.close()
warnings.filterwarnings(action='ignore')

# task5의 core별 수행능력

# 최댓값, 최솟값, 평균값을 행으로 추가하는 방식으로 진행하기 위해 재정렬을 진행하는 과정
task5_core = data.loc[:,'task5'] # task5 기준으로 core들을 모두 가져옴
# print(task5_core)

task5_core1 = pd.to_numeric(task5_core["core1"]) # task5 기준 core1 나열(to_numeric함수 사용하여 자료형 int로 변경 > 최솟값과 최댓값을 찾아내지 못하는 문제 발생 > 자료형 문제였음)
task5_core1_rename = task5_core1.rename(index={"core1":"task5"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task5으로 통일
task5_core2 = pd.to_numeric(task5_core["core2"]) # task5 기준 core2 나열
task5_core2_rename = task5_core2.rename(index={"core2":"task5"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task5으로 통일
task5_core3 = pd.to_numeric(task5_core["core3"]) # task5 기준 core3 나열
task5_core3_rename = task5_core3.rename(index={"core3":"task5"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task5으로 통일
task5_core4 = pd.to_numeric(task5_core["core4"]) # task5 기준 core4 나열
task5_core4_rename = task5_core4.rename(index={"core4":"task5"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task5으로 통일
task5_core5 = pd.to_numeric(task5_core["core5"]) # task5 기준 core5 나열
task5_core5_rename = task5_core5.rename(index={"core5":"task5"}) #시리즈를 합치기 위해 열 이름을 기준이 되는 task5으로 통일

task5_core_realignment = pd.concat([task5_core1_rename,task5_core2_rename,task5_core3_rename,task5_core4_rename,task5_core5_rename],axis=1,keys=['core1','core2','core3','core4','core5'])
# print(task5_core_realignment) # task5의 core별로 재정렬 진행 완료

task5_core_max_arr = [] # max 배열 생성
task5_core_min_arr = [] # min 배열 생성
task5_core_mean_arr = [] # mean 배열 생성

task5_core1_max = task5_core_realignment["core1"].max() # task5 기준 core1 최댓값
task5_core_max_arr.insert(0,task5_core1_max) # 배열에 0번째로 삽입
task5_core2_max = task5_core_realignment["core2"].max() # task5 기준 core2 최댓값
task5_core_max_arr.insert(1,task5_core2_max) # 배열에 1번째로 삽입
task5_core3_max = task5_core_realignment["core3"].max() # task5 기준 core3 최댓값
task5_core_max_arr.insert(2,task5_core3_max) # 배열에 2번째로 삽입
task5_core4_max = task5_core_realignment["core4"].max() # task5 기준 core4 최댓값
task5_core_max_arr.insert(3,task5_core4_max) # 배열에 3번째로 삽입
task5_core5_max = task5_core_realignment["core5"].max() # task5 기준 core5 최댓값
task5_core_max_arr.insert(4,task5_core5_max) # 배열에 4번째로 삽입
# print(task5_core_max_arr)

task5_core1_min = task5_core_realignment["core1"].min() # task5 기준 core1 최솟값
task5_core_min_arr.insert(0,task5_core1_min) # 배열에 0번째로 삽입
task5_core2_min = task5_core_realignment["core2"].min() # task5 기준 core2 최솟값
task5_core_min_arr.insert(1,task5_core2_min) # 배열에 1번째로 삽입
task5_core3_min = task5_core_realignment["core3"].min() # task5 기준 core3 최솟값
task5_core_min_arr.insert(2,task5_core3_min) # 배열에 2번째로 삽입
task5_core4_min = task5_core_realignment["core4"].min() # task5 기준 core4 최솟값
task5_core_min_arr.insert(3,task5_core4_min) # 배열에 3번째로 삽입
task5_core5_min = task5_core_realignment["core5"].min() # task5 기준 core5 최솟값
task5_core_min_arr.insert(4,task5_core5_min) # 배열에 4번째로 삽입
# print(task5_core_min_arr)

task5_core1_mean = task5_core_realignment["core1"].mean() # task5 기준 core1 평균값
task5_core_mean_arr.insert(0,task5_core1_mean) # 배열에 0번째로 삽입
task5_core2_mean = task5_core_realignment["core2"].mean() # task5 기준 core2 평균값
task5_core_mean_arr.insert(1,task5_core2_mean) # 배열에 1번째로 삽입
task5_core3_mean = task5_core_realignment["core3"].mean() # task5 기준 core3 평균값
task5_core_mean_arr.insert(2,task5_core3_mean) # 배열에 2번째로 삽입
task5_core4_mean = task5_core_realignment["core4"].mean() # task5 기준 core4 평균값
task5_core_mean_arr.insert(3,task5_core4_mean) # 배열에 3번째로 삽입
task5_core5_mean = task5_core_realignment["core5"].mean() # task5 기준 core5 평균값
task5_core_mean_arr.insert(4,task5_core5_mean) # 배열에 4번째로 삽입
# print(task5_core_mean_arr)

task5_core_realignment.loc['avg'] = task5_core_mean_arr # mean행 추가
task5_core_realignment.loc['max'] = task5_core_max_arr # max행 추가
task5_core_realignment.loc['min'] = task5_core_min_arr # min행 추가
# print(task5_core_realignment)

task5_core_realignment = task5_core_realignment.loc[['avg','max','min']]
task5_core_realignment = task5_core_realignment.transpose()
# print(task5_core_realignment)

task5_core_realignment = task5_core_realignment.astype(float)
task5_core_realignment.plot()
plt.title('20191412 강수정')
plt.suptitle('task5의 core별 수행능력', fontsize=15)
plt.savefig('task5_core.png')
plt.close()
warnings.filterwarnings(action='ignore')