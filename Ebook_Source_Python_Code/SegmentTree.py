
#세그먼트 트리 초기화
def initsegment(left,right,treeindex):
    global segmentmaxindex,origin,segmenttree
    if left == right:
        if segmentmaxindex < treeindex:
            segmentmaxindex = treeindex
        segmenttree[treeindex] = origin[left]
        return segmenttree[treeindex]
    else:
        mid = int((left + right) / 2)
        segmenttree[treeindex] = initsegment(left,mid,2 * treeindex) + initsegment(mid + 1,right,2 * treeindex + 1)
        return segmenttree[treeindex]

#def findsum(left,right,first,second):



def printsum(left,right):
    first=int(input("배열의 구간 합 첫 번째 범위 : "))
    second=int(input("배열의 구간 합 두 번째 범위 : "))
    if first>second:
        first,second=second,first



origin = [4, 7, 1, -3, 10, -1, 6]
segmenttree = [0 for i in range(4 * len(origin))]
#세그먼트 트리의 최대 인덱스
segmentmaxindex = 0
#세그먼트 트리의 루트 인덱스(모든 원소의 합인 인덱스)
segmentindex = 1

initsegment(0,len(origin) - 1,segmentindex)

printsum(0,len(origin) - 1)