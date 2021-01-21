
def printmatrix(self):          #그래프 출력
    for i in range(0,len(self)):
        print(self[i],end="\n\n")
    print()

undirected=[[0,1,1,0], [1,0,0,1], [1,0,0,1], [0,1,1,0]]
directed=[[0,1,1,0], [0,0,0,1], [0,0,0,1], [0,1,1,0]]
weighted=[[0,7,2,0], [7,0,0,5], [2,0,0,10], [0,5,10,0]]

print("무 방향 그래프\n")
printmatrix(undirected)
print("방향 그래프\n")
printmatrix(directed)
print("가중치 그래프\n")
printmatrix(weighted)

