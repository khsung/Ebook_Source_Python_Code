
import heapq

num=[6,3,5,7,9,1,6]
heap=[]

for i in num:
    heapq.heappush(heap,(-i,i))

while heap:
    print(heapq.heappop(heap)[1], end=" ")

