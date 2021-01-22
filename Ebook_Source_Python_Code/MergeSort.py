
#왼쪽과 오른쪽 두개의 배열을 정렬하면서 합침
def Merge(self, left, mid, right):
    #정렬을 위한 임시 저장 배열
    temp = [0]*len(array)
    l = left
    m = mid + 1
    tempindex=left

    #한쪽의 배열의 크기가 0이 될 때까지
    #두개의 배열 중 작은 원소를 임시배열에 저장
    while l <= mid and m <= right:
        if array[l] < array[m]:
            temp[tempindex] = array[l]
            tempindex += 1
            l += 1
        else:
            temp[tempindex] = array[m]
            tempindex += 1
            m += 1

    #남은 배열은 임시배열에 저장된 원소들 보다
    #큰 원소들이 오름차순 정렬되어 있으므로
    #차례로 임시배열에 넣어준다
    #m > right는 왼쪽 배열이 남아있는 경우
    if m > right:
        while l <= mid:
            temp[tempindex] = array[l]
            tempindex += 1
            l += 1

    #오른쪽 배열이 남아있는 경우
    else:
        while m <= right:
            temp[tempindex] = array[m]
            tempindex += 1
            m += 1

    #임시 배열을 원래 배열에 저장
    for i in range(left,right+1):
        self[i]=temp[i]
    print("temp 배열 :",temp)
    print("원래 배열 :",self,end ="\n\n")

def MergeSort(self, left, right):
    if left < right:
        #Python에서는 나눗셈 시
        #자동으로 실수형 변환이 되므로
        #int형으로 형변환 시켜준다
        mid = (int)((left+right)/2)

        #mid를 기준으로 두개의 배열로 나눔
        #배열크기가 2라면 굳이 재귀함수를
        #호출하지 않음
        if left+1 != right:
            #왼쪽 배열
            MergeSort(self, left, mid)
            #오른쪽 배열
            MergeSort(self, mid+1, right)
        #두개의 배열을 정렬하면서 합침
        Merge(self, left, mid, right)

array=[5, 4, 2, 3, 1]
print("정렬 전 배열 :",array)
print("\n병합 정렬 과정")
MergeSort(array, 0, len(array)-1)
print("정렬 된 배열 :",array)