
INF = float('inf')

graph = [[0,2,8,5,INF],
       [2,0,INF,1,9],
       [8,INF,0,2,INF],
       [5,1,2,0,4],
       [INF,9,INF,4,0]]
MST_edge = []

#간선 정보 변수 선언 [시작 노드, 도착 노드, 가중치] 형태로 저장 예정
edgeinfo = []

#그래프 출력하면서 간선 정보 저장
#무 방향 그래프이므로 시작 노드의 번호가 도착 노드의 번호보다
#더 적게 간선을 저장
print("행렬 그래프")
for i in range(len(graph)):
    for j in range(len(graph[i])):
        print(graph[i][j],end=" ")
        if graph[i][j] != INF and i < j:
            edgeinfo.append([i,j,graph[i][j]])
    print()

#간선들의 가중치를 기준으로 오름차순 정렬
#lambda는 다차원 리스트에서 특정 원소로 정렬하는 파이썬의 내장 함수
#x:x[2]는 인덱스 2를 기준으로 리스트 정렬하겠단 의미
edgeinfo.sort(key=lambda x:x[2])

print("edgeinfo : ",edgeinfo)
#union-find 알고리즘을 위한 리스트 초기화
union_find = []
for i in range(len(graph)):
    union_find.append(i)

for i in range(len(edgeinfo)):
    print("union_find : ",union_find)
    if (union_find[edgeinfo[i][0]]) != (union_find[edgeinfo[i][1]]):
        union_find[edgeinfo[i][1]] = union_find[edgeinfo[i][0]]
        MST_edge.append(edgeinfo[i])
        #재귀적으로 부모노드를 찾아야함
        #while 

print(MST_edge)