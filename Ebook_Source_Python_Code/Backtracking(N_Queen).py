
def addAtackLine(self, row, column, N):
    for i in range(N):
        self[row][i] += 1
        self[i][column] += 1
    self[row][column] -= 1

    #오른쪽 위
    r = row - 1
    c = column + 1
    while r<N and r>=0 and c<N and c>=0:
        self[r][c] += 1
        r -= 1
        c += 1

    #오른쪽 아래
    r = row + 1
    c = column + 1
    while r<N and r>=0 and c<N and c>=0:
        self[r][c] += 1
        r += 1
        c += 1

    #왼쪽 위
    r = row - 1
    c = column - 1
    while r<N and r>=0 and c<N and c>=0:
        self[r][c] += 1
        r -= 1
        c -= 1

    #왼쪽 아래
    r = row + 1
    c = column - 1
    while r<N and r>=0 and c<N and c>=0:
        self[r][c] += 1
        r += 1
        c -= 1

def delAtackLine(self, row, column, N):
    for i in range(N):
        self[row][i] -= 1
        self[i][column] -= 1
    self[row][column] += 1
    
    #오른쪽 위
    r = row - 1
    c = column + 1
    while r<N and r>=0 and c<N and c>=0:
        self[r][c] -= 1
        r -= 1
        c += 1

    #오른쪽 아래
    r = row + 1
    c = column + 1
    while r<N and r>=0 and c<N and c>=0:
        self[r][c] -= 1
        r += 1
        c += 1

    #왼쪽 위
    r = row - 1
    c = column - 1
    while r<N and r>=0 and c<N and c>=0:
        self[r][c] -= 1
        r -= 1
        c -= 1

    #왼쪽 아래
    r = row + 1
    c = column - 1
    while r<N and r>=0 and c<N and c>=0:
        self[r][c] -= 1
        r += 1
        c -= 1

def N_Queen(self, row, N):
    global count
    #첫 번째 행부터 탐색
    if row < N-1:
        #해당 행에 퀸이 위치 가능한 열 검색
        for i in range(N):
            if self[row][i] == 0:
                #공격 라인 추가
                addAtackLine(self, row, i, N)
                N_Queen(self, row+1, N)
                #공격 라인 제거, 이 과정이 백트래킹
                delAtackLine(self, row, i, N)

    #마지막 행일 경우
    else:
        for i in range(N):
            if self[row][i] == 0:
                count+=1

count=0
num=int(input("Input N : "))
#입력받은 크기만큼 2차원 배열 선언
chess=[[0]*num for i in range(num)]
N_Queen(chess, 0, num)
print("퀸을 놓을 수 있는 경우의 수 :",count)

