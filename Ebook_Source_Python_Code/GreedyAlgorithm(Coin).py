
coinValue=[500, 100, 50, 10]  #동전 금액
coinCount=[0, 0, 0, 0]        #지불할 동전 개수
cost=int(input("지불 금액 : "))

for i in range(len(coinValue)):
    #최대한 적은 개수를 내기 위해 가장 큰 금액의
    #동전부터 처리, 그리디 알고리즘의 핵심원리
    while coinValue[i]<=cost:
        cost-=coinValue[i]
        coinCount[i]+=1

#각 동전의 개수 출력
for i in range(len(coinValue)):
    print(coinValue[i],"원 동전의 개수 :",coinCount[i])

