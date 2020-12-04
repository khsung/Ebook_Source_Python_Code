
array=[4,1,0,4,2,1,2]
countarray=[0,0,0,0,0,0,0]
print("정렬 전 리스트 : ",array)
print("\n정렬과정")
#리스트 원소값의 
#countarray 인덱스에 1씩 더하기
for i in range(0,len(array)):
    countarray[array[i]]+=1  

array=[]           #원래 리스트 초기화

for i in range(0,len(countarray)):
    while countarray[i]>0:  #countarray의 원소가
        array.append(i)     #0이 될때까지 인덱스값을
        countarray[i]-=1    #원래 리스트에 추가해줌
        print(array)
print("\n정렬 된 리스트 : ",array)

