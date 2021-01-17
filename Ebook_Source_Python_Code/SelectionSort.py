
data=[2,3,1,5,4]
print("정렬 전 배열 :",data)
print("정렬 과정")
for i in range(0, len(data)-1):
    min=i               #최솟값 찾기 위한 변수 
    for j in range(i,len(data)):
        if data[min]>data[j]:
            min=j
    #최솟값과 정렬할 인덱스가 다를 경우만 교환
    if i!=min:
        data[i],data[min]=data[min],data[i]
    print(data)
print("정렬 된 배열 :",data)

