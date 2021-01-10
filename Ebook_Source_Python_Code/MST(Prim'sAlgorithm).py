
INF = float('inf')

#그래프 행렬
graph = [[0,2,8,5,INF],
         [2,0,INF,1,9],
         [8,INF,0,2,INF],
         [5,1,2,0,4],
         [INF,9,INF,4,0]]

startnode = 0
#최소 신장 트리 간선 정보 저장, [노드,노드,가중치]
MST = []
#MST로 확정된 노드들 추가
visited = []
print("MST 간선 추가 과정")

#마지막 노드는 그냥 추가만 하면 되므로 N-1개의 노드를 방문할 때까지 반복
while len(visited) < len(graph) - 1:
    #방문한 노드로 추가
    visited.append(startnode)
    #최소 비용의 간선 찾기 위해 무한대로 변수 선언
    min = INF
    #방문한 노드 개수만큼 반복
    for i in range(len(visited)):
        for j in range(len(graph[visited[i]])):
            #방문하지 않은 노드면서 비용이 가장 적은 간선 저장
            if graph[visited[i]][j] < min and visited.count(j) == 0:
                min = graph[visited[i]][j]
                firstnode = visited[i]
                secondnode = j
    #저장 가능한 간선 중 가중치가 가장 적은 간선 저장
    MST.append([firstnode,secondnode,min])
    print(MST)
    startnode = secondnode

#최소 신장 트리의 비용 합
costsum = 0
print("\n최종 MST 간선 정보")
for i in range(len(MST)):
    print("노드",MST[i][0],"노드",MST[i][1],"가중치 :",MST[i][2])
    costsum+=MST[i][2]
print("\n최종 비용 :",costsum)
