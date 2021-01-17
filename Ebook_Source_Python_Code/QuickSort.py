def quicksort(arr):
    if len(arr) < 2:            #리스트의 크기가 1일 때
        return arr              #리스트 반환
    else:
        pivot = 0               #첫 번째 원소 pivot설정
                                #원하는 원소를 정해도 됨
        left = 1                #pivot 다음 원소
        right = len(arr) - 1    #리스트 끝 원소
        print("\nPivot : ",arr[pivot])
        print(arr,"->",end=" ")
        while left < right:     #left와 right가 엇갈릴 때까지 반복
            if arr[left] < arr[pivot]:
                left += 1
            elif arr[right] > arr[pivot]:
                right -= 1
            #left가 pivot보다 크고 right가 pivot보다 작을 경우 교환
            else:
                arr[left],arr[right] = arr[right],arr[left]

        #첫 번째 원소를 pivot으로 정했으므로 pivot보다 작은 원소들 중
        #가장 오른쪽에 있는 원소와 pivot의 값 교환
        if arr[left] < arr[pivot]:
            arr[left],arr[pivot] = arr[pivot],arr[left]
        else:
            arr[left - 1],arr[pivot] = arr[pivot],arr[left - 1]
        print(arr)

        #왼쪽 리스트, 오른쪽 리스트로 나누어
        #각각 길이가 1 이하가 될 때까지 반복
        return quicksort(arr[:left]) + quicksort(arr[right:])

arr = [5,1,3,7,6,2,4]
print("정렬 전 배열 : ",arr)
print("\n퀵 정렬 과정")
print("\n정렬 된 배열 : ",quicksort(arr))