
def p(self, N):
    for i in range(N):
        print(self[i])

def addAtackLine(self, row, column, N):
    r=row
    c=column
    for i in range(N):
        self[row][i] += 1
        self[i][column] += 1
    if r - c >= 0:
        r = r - c
        c = c - c
    else:
        r = r - r
        c = c - r
    while r < N and c < N:
        self[r][c] += 1
        r += 1
        c += 1
    self[row][column] -= 2

def delAtackLine(self, row, column, N):
    r=row
    c=column
    for i in range(N):
        self[row][i] -= 1
        self[i][column] -= 1
    if r - c >= 0:
        r = r - c
        c = c - c
    else:
        r = r - r
        c = c - r
    while r < N and c < N:
        self[r][c] -= 1
        r += 1
        c += 1
    self[row][column] += 2

def N_Queen(self, row, N):
    global count
    print("row = ",row)
    p(self,N)
    if row < N-1:
        for i in range(N):
            if self[row][i] == 0:
                addAtackLine(self, row, i, N)
                N_Queen(self, row+1, N)
                delAtackLine(self, row, i, N)

    else:
        for i in range(N):
            if self[row][i] == 0:
                count+=1



count=0
num=int(input("Input N : "))
chess=[[0]*num for i in range(num)]
N_Queen(chess, 0, num)

#for i in range(num):
#    print(chess[i])
print(count)

