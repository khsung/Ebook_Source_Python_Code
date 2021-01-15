
import math     #수학연산을 위한 math모듈
searchlist = [1, 2, 3, 4, 5, 6, 7]
left = 0
right = len(searchlist) - 1
print("기존 리스트 :",searchlist)

for i in range(2):
    check = False     #원소가 있는지 체크하는 변수
    answer = int(input("찾을 원소 : "))
    while left <= right:
        mid = math.floor((right + left) / 2)  #중간 인덱스 정수로 계산
        if searchlist[mid] == answer:
            print(searchlist[mid],"검색 완료, 인덱스 :",mid)
            check = True
            break
        #중간 값보다 찾을 값이 더 작을 경우
        elif searchlist[mid] > answer:
            right = mid - 1
        #중간 값보다 찾을 값이 더 클 경우
        else:
            left = mid + 1
    if check == False:
        print("해당 원소 없음")

