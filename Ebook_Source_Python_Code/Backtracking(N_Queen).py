
def addAtackLine(self, row, column, N):
    #퀸이 놓인 위치를 기준으로 가로 세로 공격라인 추가
    for i in range(N):
        self[row][i] += 1
        self[i][column] += 1
    self[row][column] -= 1

    #퀸의 오른쪽 위
    r = row - 1
    c = column + 1
    while r < N and r >= 0 and c < N and c >= 0:
        self[r][c] += 1
        r -= 1
        c += 1

    #퀸의 오른쪽 아래
    r = row + 1
    c = column + 1
    while r < N and r >= 0 and c < N and c >= 0:
        self[r][c] += 1
        r += 1
        c += 1

    #퀸의 왼쪽 위
    r = row - 1
    c = column - 1
    while r < N and r >= 0 and c < N and c >= 0:
        self[r][c] += 1
        r -= 1
        c -= 1

    #퀸의 왼쪽 아래
    r = row + 1
    c = column - 1
    while r < N and r >= 0 and c < N and c >= 0:
        self[r][c] += 1
        r += 1
        c -= 1

def delAtackLine(self, row, column, N):
    #퀸이 놓인 위치를 기준으로 가로 세로 공격라인 제거
    for i in range(N):
        self[row][i] -= 1
        self[i][column] -= 1
    self[row][column] += 1
    
    #퀸의 오른쪽 위
    r = row - 1
    c = column + 1
    while r < N and r >= 0 and c < N and c >= 0:
        self[r][c] -= 1
        r -= 1
        c += 1

    #퀸의 오른쪽 아래
    r = row + 1
    c = column + 1
    while r < N and r >= 0 and c < N and c >= 0:
        self[r][c] -= 1
        r += 1
        c += 1

    #퀸의 왼쪽 위
    r = row - 1
    c = column - 1
    while r < N and r >= 0 and c < N and c >= 0:
        self[r][c] -= 1
        r -= 1
        c -= 1

    #퀸의 왼쪽 아래
    r = row + 1
    c = column - 1
    while r < N and r >= 0 and c < N and c >= 0:
        self[r][c] -= 1
        r += 1
        c -= 1

def N_Queen(self, row, N):
    global count
    #첫 번째 행부터 탐색
    if row < N - 1:
        #해당 행에 퀸이 위치 가능한 열 검색
        for i in range(N):
            if self[row][i] == 0:
                #공격 라인 추가
                addAtackLine(self, row, i, N)
                N_Queen(self, row + 1, N)
                #공격 라인 제거, 이 과정이 백트래킹
                delAtackLine(self, row, i, N)

    #마지막 행일 경우
    else:
        for i in range(N):
            if self[row][i] == 0:
                count+=1

#실행해 본 결과 너무 오래 걸려 N이 12일 때까지만 결과 출력
for i in range(13):
    count = 0
    chess = [[0] * i for j in range(i)]
    print("N이",i,"일 때",end=" ")
    N_Queen(chess, 0, i)
    print("퀸을 놓을 수 있는 경우의 수 :",count,end="\n\n")

