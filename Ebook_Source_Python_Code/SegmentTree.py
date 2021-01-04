
#세그먼트 트리 초기화
#left : 세그먼트 트리 구간의 왼쪽 인덱스, right : 세그먼트 트리 구간의 오른쪽 인덱스
def initsegment(left,right,segmentindex):
    global segmentmaxindex,origin,segmenttree     #전역 변수 선언
    #하나의 인덱스만 포함하는 노드일 경우
    if left == right:
        #세그먼트 트리 최대 인덱스 갱신
        if segmentmaxindex < segmentindex:
            segmentmaxindex = segmentindex
        segmenttree[segmentindex] = origin[left]
        return segmenttree[segmentindex]
    else:
        mid = int((left + right) / 2)
        #왼쪽 자식노드와 오른쪽 자식노드의 합을 저장하고 반환
        segmenttree[segmentindex] = initsegment(left,mid,2 * segmentindex) + initsegment(mid + 1,right,2 * segmentindex + 1)
        return segmenttree[segmentindex]

#범위 합을 구하는 함수
def findsum(left,right,first,second,segmentindex):
    mid = int((left + right) / 2)
    #현재 노드의 구간일 경우
    if left == first and right == second:
        return segmenttree[segmentindex]
    #왼쪽 자식 노드에만 포함되는 경우
    elif second <= mid:
        return findsum(left,mid,first,second,2 * segmentindex)
    #오른쪽 자식 노드에만 포함되는 경우
    elif mid + 1 <= first:
        return findsum(mid + 1,right,first,second,2 * segmentindex + 1)
    #왼쪽 자식, 오른쪽 자식 둘다에 포함되는 구간일 경우
    else:
        sum = findsum(left,mid,first,mid,2 * segmentindex) + findsum(mid + 1,right,mid + 1,second,2 * segmentindex + 1)
        return sum

#범위 합 출력 함수
def printsum(left,right,segmentindex):
    first = int(input("\n배열의 구간 합 첫 번째 범위 : "))
    second = int(input("배열의 구간 합 두 번째 범위 : "))
    if first > second:
        first,second = second,first
    answer = findsum(left,right,first,second,segmentindex)
    print("인덱스",first,"부터 인덱스",second,"까지의 합 :",answer)

#세그먼트 트리 갱신
def updatesegment(left,right,segmentindex,arrayindex,diff):
    #현재 노드가 변경된 배열의 인덱스 하나만 포함하는 경우
    if left == right and left == arrayindex:
        segmenttree[segmentindex]+=diff
    else:
        segmenttree[segmentindex]+=diff
        mid = int((left + right) / 2)
        #변경된 배열의 인덱스가 왼쪽 자식에 포함될 경우
        if arrayindex <= mid:
            updatesegment(left,mid,2 * segmentindex,arrayindex,diff)
        #변경된 배열의 인덱스가 오른쪽 자식에 포함될 경우
        else:
            updatesegment(mid + 1,right,2 * segmentindex + 1,arrayindex,diff)

origin = [4, 7, 1, -3, 10, -1, 6]
segmenttree = [0 for i in range(4 * len(origin))]
#세그먼트 트리의 최대 인덱스
segmentmaxindex = 0
#세그먼트 트리의 루트 인덱스(모든 원소의 합인 인덱스)
segmentindex = 1

initsegment(0,len(origin) - 1,segmentindex)
print("세그먼트 트리의 최대 인덱스",segmentmaxindex)
printsum(0,len(origin) - 1,segmentindex)

print("\n배열값을 변경 할 인덱스 위치(",0,"~",len(origin) - 1,") : ",end="")
changevalueindex = int(input())
#변경 전 값 저장
originvalue = origin[changevalueindex]
origin[changevalueindex] = int(input("변경할 값 : "))
difference = origin[changevalueindex] - originvalue

updatesegment(0,len(origin) - 1,segmentindex,changevalueindex,difference)
printsum(0,len(origin) - 1,segmentindex)