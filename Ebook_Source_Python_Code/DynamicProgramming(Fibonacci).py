
Recursivecount = 0              #재귀 알고리즘 실행 횟수
DPcount = 0                     #동적 계획법 실행 횟수

#재귀 알고리즘
def RecursiveFibonacci(num):
    global Recursivecount       #전역 변수 선언
    Recursivecount += 1
    # 1번째 숫자 : 0, 2번째 숫자 : 1 (인덱스는 0부터 시작하므로)
    if num - 1 == 0 or num - 1 == 1:
        return num - 1
    else:
        #재귀를 통해 매번 계산을 해야됨 = 숫자가 커지면 오버헤드
        return RecursiveFibonacci(num - 1) + RecursiveFibonacci(num - 2)

#동적 계획법 (Dynamic Programming)
def DPFibonacci(num):
    global DPcount              #전역 변수 선언
    DPcount += 1
    # 1번째 숫자 : 0, 2번째 숫자 : 1 (인덱스는 0부터 시작하므로)
    if num - 1 == 0 or num - 1 == 1:
        DP[num - 1] = num - 1
        return DP[num - 1]

    #계산된 값이 있을 경우 계산 없이 값만 리턴
    elif DP[num - 1] > 0:
        return DP[num - 1]
    else:
    #계산된 값이 없을 경우 재귀를 통해 연산값 저장 후 리턴
        DP[num - 1] = DPFibonacci(num - 1) + DPFibonacci(num - 2)
        return DP[num - 1]

num = 10  #10번째 자리, 20 으로도 실행
DP = [0 for i in range(num)]  #num 크기만큼 0으로 초기화
print("재귀 알고리즘 피보나치 수열의",num,"번째 숫자 :",RecursiveFibonacci(num))
print("재귀 알고리즘 연산 횟수",Recursivecount)
print("\n동적 계획법 피보나치 수열의",num,"번째 숫자 :",DPFibonacci(num))
print("동적 프로그래밍 연산 횟수",DPcount)
