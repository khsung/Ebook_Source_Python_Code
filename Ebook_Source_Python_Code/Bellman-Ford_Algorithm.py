
def bellman_ford(graph,cost,startnode,edgeinfo):
    #노드 개수만큼 반복
    for i in range(len(graph)):
        #모든 간선을 고려
        for j in range(len(edgeinfo)):
            curr=edgeinfo[j][0]
            next=edgeinfo[j][1]
            edgecost=edgeinfo[j][2]
            #현재 노드와 다음 노드까지의 비용을 더한 값이 비용 리스트에 저장되어 있는
            #다음 노드까지의 비용보다 적을 경우 갱신 
            if cost[next]>cost[curr]+edgecost:
                cost[next]=cost[curr]+edgecost  
                #마지막 노드에서도 비용이 갱신 된다면 음의 순환이 존재한다는 의미
                if i == len(graph)-1:
                    return False
        #매번 갱신된 비용 리스트 출력
        print(cost)
    #음의 순환이 존재하지 않을 경우 True 반환
    return True

#음수 순환인지 아닌지 출력하는 함수
def judgecycle(result):
    if result == True:
        print("\n음의 순환이 없는 그래프")
        print("비용 :",cost,end="\n\n")
    else:
        print("\n음의 순환이 있는 그래프",end="\n\n")

inf = float("inf")   #무한대 변수 선언

graph = [[0,6,4,9,inf],                 #음의 순환이 없는 그래프
         [-3,0,inf,1,6],
         [-3,inf,0,2,inf],
         [inf,inf,inf,0,4],
         [inf,2,inf,inf,0]]

#간선 정보 배열 [시작 노드, 도착 노드, 가중치] 형태로 저장 예정
edgeinfo=[]
cost = [inf] * len(graph)       #비용 초기화
startnode = 0                   #시작 노드
cost[startnode] = 0             #시작 노드 비용 갱신

print("첫 번째 그래프 행렬")
#그래프 출력하면서 각 노드별 간선 정보 저장
for i in range(len(graph)):
    for j in range(len(graph[i])):
        print(graph[i][j],end=" ")
        if graph[i][j] != 0 and graph[i][j] != inf:
            edgeinfo.append([i, j, graph[i][j]])
    print()

print("\n비용 갱신 과정")
res=bellman_ford(graph,cost,startnode,edgeinfo)
judgecycle(res)

cyclegraph = [[0,6,4,9,inf],            #음의 순환이 있는 그래프
              [-30,0,inf,1,6],
              [-3,inf,0,2,inf],
              [inf,inf,inf,0,4],
              [inf,2,inf,inf,0]]

edgeinfo=[]                     #간선 정보 배열 초기화
cost = [inf] * len(graph)       #비용 초기화
cost[startnode] = 0             #시작 노드 비용 갱신

print("두 번째 그래프 행렬")
#그래프 출력하면서 각 노드별 간선 정보 저장
for i in range(len(cyclegraph)):
    for j in range(len(cyclegraph[i])):
        print(cyclegraph[i][j],end=" ")
        if cyclegraph[i][j] != 0 and cyclegraph[i][j] != inf:
            edgeinfo.append([i, j, cyclegraph[i][j]])
    print()

print("\n비용 갱신 과정")
res=bellman_ford(cyclegraph,cost,startnode,edgeinfo)
judgecycle(res)
