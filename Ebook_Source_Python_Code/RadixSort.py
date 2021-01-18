
#원소들의 최대 자리수 찾기
def findMaxDigit(self):
    maxdigit = 0
    for i in self:
        temp = i
        count = 0
        #자리수만큼 count 증가
        while(temp > 0):
            temp = int(temp / 10)
            count+=1
        if count > maxdigit:
            maxdigit = count
    return maxdigit

#정렬 할 배열
array = [541, 303, 9, 70, 5, 47, 11, 3, 155]
#0부터 9까지 인덱스를 위한 빈 리스트 생성
queue = [[] for i in range(10)]

#currdigit은 현재 자리수
currdigit = 1
print("정렬 전 배열 : ",array)
print("\n기수 정렬 과정")
for i in range(0, findMaxDigit(array)):
    for j in array:
        queue[(int(j / currdigit)) % 10].append(j)
    array = []

    #큐에 있는 원소들을 원래 리스트로 재정렬
    for j in range(0,10):
        while(len(queue[j]) > 0):
            array.append(queue[j][0])
            queue[j].pop(0)
    print(array)
    currdigit = currdigit * 10
print("\n정렬 된 배열 : ",array)

