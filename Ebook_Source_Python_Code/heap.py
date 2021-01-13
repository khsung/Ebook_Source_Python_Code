
import heapq

num=[6,3,5,7,9,1,6]
heap=[]

print("리스트 :",num)

#(-값, 값)은 원래 값을 음수 형태로 첫 번째 인덱스에
#저장하여 오름차순으로 정렬하면 두 번째 인덱스는
#자동으로 내림차순 형태로 저장되는 원리를 사용한 것
for i in num:
    heapq.heappush(heap,(-i,i))
print("최대 힙 : ",end="")

#두 번째 인덱스의 값(원래 값)을 출력
while heap:
    print(heapq.heappop(heap)[1], end=" ")
print()

