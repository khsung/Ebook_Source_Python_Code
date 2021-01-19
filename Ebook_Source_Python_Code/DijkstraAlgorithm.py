
inf = float("inf")  #무한대(InfInity) 변수 선언
#그래프 행렬 선언
graph = [[0,2,8,5,inf],
         [2,0,inf,1,9],
         [8,inf,0,2,inf],
         [5,1,2,0,4],
         [inf,9,inf,4,0]]

startnode = 0       #시작 노드
savestart = startnode   #차후에 쓰기위해 시작 노드 저장
visited = [False] * len(graph)   #방문한 노드인지 체크하는 리스트
cost = [inf] * len(graph)        #무한대로 비용설정

#리스트의 인덱스로 경로 저장, 예를 들어 path=[0,0,1]이라면 노드를 기준으로
#0(인덱스) -> 0(값), 1(인덱스) -> 0(값)(인덱스) -> 0(값), 2(인덱스) -> 1(값)(인덱스) -> 0(값)을 뜻한다
path = [inf] * len(graph)

cost[startnode] = graph[startnode][startnode]   #비용을 저장하는 리스트
path[startnode] = startnode                     #경로를 저장하는 리스트

#그래프 출력
print("그래프 행렬")
for i in range(len(graph)):
    print(graph[i])

print("\n초기 비용")
print(cost)

#그래프 노드 개수만큼 반복
for i in range(len(graph)):
    print("\n시작 노드 :",startnode)
    for j in range(len(graph[startnode])):
        #방문 하지 않은 인접 노드 중 비용이 더 적을 경우 비용과 경로 리스트 갱신
        if ((visited[j] == False) and (j != inf) and (cost[startnode] + graph[startnode][j] < cost[j])):
            cost[j] = cost[startnode] + graph[startnode][j]
            path[j] = startnode

    #방문한 노드로 표시
    visited[startnode] = True
    min = inf
    print("갱신된 비용 :",cost)
    for j in range(len(graph[startnode])):
        #방문 안한 노드 중 비용이 가장 작은 노드 선택
        if (visited[j] == False) and (cost[j] < min):
            min = cost[j]

    #min이 inf인 경우는 모든 노드를 방문한 경우
    if min != inf:
        #최소값을 가진 노드를 시작노드로 선택
        startnode = cost.index(min)

print("\n경로 배열")
print(path)
print()
startnode = savestart         #원래 시작노드로 초기화

#각 노드의 최소 비용 경로 출력
for i in range(len(graph)):
    print("목적지 노드 :",i,end="   ")
    print("최소비용 경로",end="   ")
    print(i,end="")
    temp = path[i]

    while temp != startnode:
        print(" <-",temp,end="")
        temp = path[temp]
    if i != startnode:
        print(" <-",temp,end="")
        temp = path[temp]
    print("\n")