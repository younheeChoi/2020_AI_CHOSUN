test_a=3
if test_a == 3:
    print('3')
else:
    print('3이 아닙니다.')

for i in range(0,10):
    print(i)

temp=0
while True:
    temp= temp+1
    print(temp)
    if temp > 40: #temp가 40 넘어갈시 종료
        break

temp=0
while temp<40: #temp값이 40보다 작은경우를 나열해
    temp+=1 #temp값은 1씩 점점 늘릴거야.
    print(temp)

#y=f(x)
def 최윤희(x): #x값을 받는 최윤희 함수 정의
    y=x+3 #받은 x값을 이용해서 y를 구함
    return y #y값을 리턴할거야

print(최윤희(3))