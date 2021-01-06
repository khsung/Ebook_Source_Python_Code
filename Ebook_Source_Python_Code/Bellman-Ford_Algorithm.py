
#모든 간선을 확인해야 하는데 edgecount가 필요한가??
#3중 for문이면 될듯
def bellman_ford(graph,cost,edgecount,startnode):
    #시작 노드를 위한 반복
    for i in range(len(graph)):
        startnode=i
        for j in range(len(graph)):
            for k in range(len(graph[j])):


inf = float("inf")   #무한대 변수 선언
graph = [[0,6,4,9,inf],[-3,0,inf,1,6],[-3,inf,0,2,inf],[inf,inf,inf,0,4],[inf,2,inf,inf,0]]
#비용 초기화
cost = [0] * len(graph)
#edgecount = 0           #간선의 개수
startnode = 0           #시작 노드
cost[startnode] = 0     #시작 노드 비용 갱신

print("그래프 행렬")
#그래프 출력하면서 각 노드별 간선의 개수 추가
for i in range(len(graph)):
    #edgecount+=len(graph[i])
    #edgecount-=graph[i].count(0)     #0은 자기 자신노드
    #edgecount-=graph[i].count(inf)   #inf는 연결이 안된 노드
    print(graph[i])

bellman_ford(graph,cost,edgecount,startnode)
