
INF = float('inf')

graph = [[0,2,8,5,INF],
       [2,0,INF,1,9],
       [8,INF,0,2,INF],
       [5,1,2,0,4],
       [INF,9,INF,4,0]]

startnode = 0

MST=[]
#MST로 확정된 노드들 추가
visited = []

#모두 방문할 때까지 반복
while len(visited) < len(graph):
    visited.append(startnode)
    min = INF
    for i in range(len(visited)):
        for j in range(len(graph[visited[i]])):
            if graph[visited[i]][j] < min and visited.count(j) == 0:
                min = graph[visited[i]][j]
                firstnode = visited[i]
                secondnode = j

    MST.append([firstnode,secondnode,min])
    print(MST)
    startnode=secondnode
    
    #마지막 추가되는거 확인 필요