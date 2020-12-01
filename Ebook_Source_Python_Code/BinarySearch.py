
import math     #수학연산을 위한 math모듈

searchlist=[1,2,3,4,5,6,7]
left=0
right=len(searchlist)-1
answer=5        #원하는 원소 값
check=False     #원소가 있는지 체크하는 변수
while left<=right:
    mid=math.floor((right+left)/2)  #중심 인덱스 정수로 계산
    if searchlist[mid]==answer:
        print("정답 원소 :",searchlist[mid])
        print("정답 원소의 인덱스 :",mid)
        check=True
        break
    elif searchlist[mid]>answer:
        right=mid-1
    else:
        left=mid+1
if check==False:
    print("해당 원소 없음")

