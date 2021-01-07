

def bellman_ford(graph,cost,startnode,edgeinfo):
    for i in range(len(graph)):
        for j in range(len(edgeinfo)):
            curr=edgeinfo[j][0]
            next=edgeinfo[j][1]
            edgecost=edgeinfo[j][2]
            if cost[next]>cost[curr]+edgecost:
                cost[next]=cost[curr]+edgecost          
        print(cost)


inf = float("inf")   #무한대 변수 선언
graph = [[0,6,4,9,inf],[-3,0,inf,1,6],[-3,inf,0,2,inf],[inf,inf,inf,0,4],[inf,2,inf,inf,0]]
#간선 정보 배열 [시작 노드, 도착 노드, 가중치] 형태로 저장 예정
edgeinfo=[]
#비용 초기화
cost = [inf] * len(graph)
startnode = 0           #시작 노드
cost[startnode] = 0     #시작 노드 비용 갱신
print("그래프 행렬")
#그래프 출력하면서 각 노드별 간선 정보 저장
for i in range(len(graph)):
    for j in range(len(graph[i])):
        #print(graph[i][j],end=" ")
        if graph[i][j] != 0 and graph[i][j] != inf:
            edgeinfo.append([i, j, graph[i][j]])
    #print()
bellman_ford(graph,cost,startnode,edgeinfo)

print(cost)