
#랜덤함수를 쓰기 위한 모듈 추가
import random

#1이상 101미만의 난수 생성
answer=random.randrange(1,101)
count=1
while(answer!=count):
    print("현재 숫자 : ",count)
    count+=1
print("정답 숫자 : ",count)

