
data = [2,1,3,5,4]
print("정렬 전 배열 :",data)

print("\n삽입 정렬 과정")
for i in range(1,len(data)):
    for j in range(i - 1,-1,-1):
        #앞의 원소보다 크면 중단
        if data[j] < data[i]:
            break
        #앞의 원소보다 작으면 교환
        else:
            data[j],data[j + 1] = data[j + 1],data[j]
    print(data)
print("\n정렬 된 배열 :",data)

