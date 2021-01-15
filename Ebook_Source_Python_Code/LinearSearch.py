
check = False   #원소가 있는지 체크하는 변수
intlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("기존 리스트 :",intlist)
answer=int(input("찾을 원소 입력 : "))
for i in range(0,len(intlist)):     #첫 원소부터 끝까지 검색
    if intlist[i] == answer:        #리스트에서 원하는 원소를 찾는 코드
        print(intlist[i],"검색 완료, 인덱스 :",i)
        check = True
if check == False:                  #원소가 없을 경우
    print("해당 원소 없음")

