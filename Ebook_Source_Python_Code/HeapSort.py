
import heapq

num=[6,3,5,7,9,1,6]
heap=[]
sorted_num=[]
print("정렬 전 숫자 : ",num)
for i in num:
    heapq.heappush(heap,(-i,i))

while heap:
    sorted_num.append(heapq.heappop(heap)[1])

print("정렬 된 힙 : ",sorted_num)

