import pandas as pd

temp=pd.read_csv('data.csv')
print(temp)

print(temp['Mon']) #data중에 [Mon]만 챙겨서 불러오기_ 데이터 부분적으로 불러오기.

# 처리
# 뭔가 값을 더 추가 하고 싶어!
temp['T'] = 0 #0으로 초기화된 T를 추가
print(temp)

# 그래프 그리기
import matplotlib.pyplot as plt #그래프를 그리기 위함 함수 불러오기
plt.plot(temp['A'], dashes=[6,2])#dashes는 그래프를 점선으로 그리고 6은 칠하고 2는 공백
plt.xlim(0,5) #x의 스케일 지정
plt.ylim(0,10) #y의 스케일 지정
plt.show()