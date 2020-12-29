
inf = float("inf")  #무한대(InfInity) 변수 선언
graph=[[0,2,8,5,inf],[2,0,inf,1,9],[8,inf,0,2,inf],[5,1,2,0,4],[inf,9,inf,4,0]]
startnode=0
visited=[False]*len(graph)   #방문한 노드인지 체크하는 리스트 
cost=[inf]*len(graph)        #무한대로 비용설정

#리스트의 인덱스로 경로 저장, 예를 들어 path=[0,0,1]이라면 노드를 기준으로
#0 -> 1, (0 -> 1) -> 2를 뜻한다
path=[inf]*len(graph)

cost[startnode] = graph[startnode][startnode]
path[startnode] = startnode


for i in range(len(graph)):
    for j in range(len(graph[startnode])):
        if ((j != startnode) and (visited[j] == False) and (j != inf) and 
            (cost[startnode]+graph[startnode][j]<cost[j])):
            cost[j] = cost[startnode]+graph[startnode][j]
            path[j] = startnode
    visited[startnode] = True
    min = inf
    print(cost)
    for j in range(len(graph[startnode])):
        if (visited[j] == False) and (cost[j] < min):
            min = cost[j]
    if min != inf:
        startnode = cost.index(min)
