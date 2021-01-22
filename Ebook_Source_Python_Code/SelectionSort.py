
data = [2, 3, 1, 5, 4]
print("정렬 전 배열 :", data)

print("\n선택 정렬 과정")
for i in range(0, len(data) - 1):
    minindex = i           #최솟값 인덱스 찾기 위한 변수
    for j in range(i,len(data)):
        if data[minindex] > data[j]:
            minindex = j
    #최솟값과 정렬할 인덱스가 다를 경우만 교환
    if i != minindex:
        data[i], data[minindex] = data[minindex], data[i]
    print(data)
print("\n정렬 된 배열 :",data)

