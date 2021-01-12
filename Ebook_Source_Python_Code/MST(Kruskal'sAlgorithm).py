
#find함수, 해당 노드의 root 노드 반환
#root 노드 : 자기 자신을 가리키는 노드
def find(union_find, index):
    if union_find[index] == index:
        return index
    else:
        union_find[index] = find(union_find, union_find[index])
        return union_find[index]

#union함수, 자식 노드와 부모 노드 연결
def union(union_find, parent, child):
    parent = find(union_find,parent)
    child = find(union_find,child)
    union_find[child] = parent

INF = float('inf')      #무한대 변수 선언
#행렬 그래프
graph = [[0,2,8,5,INF],
       [2,0,INF,1,9],
       [8,INF,0,2,INF],
       [5,1,2,0,4],
       [INF,9,INF,4,0]]
#간선 정보 변수 선언 [노드 1, 노드 2, 가중치] 형태로 저장 예정
edgeinfo = []
#최소 신장 트리 간선 정보 저장
MST_edge = []

#그래프 출력하면서 간선 정보 저장
#무 방향 그래프이므로 번호가 적은 노드를 먼저 저장
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

print("\nedgeinfo : ",edgeinfo)
#union-find 알고리즘을 위한 리스트 초기화
union_find = []
for i in range(len(graph)):
    union_find.append(i)
print("초기 union_find 리스트 : ",union_find)

for i in range(len(edgeinfo)):
    #서로 root 노드가 다르다면 부모, 자식 노드로 연결하고 MST에 간선 정보 추가
    if (find(union_find,edgeinfo[i][0])) != (find(union_find,edgeinfo[i][1])):
        union(union_find, edgeinfo[i][0], edgeinfo[i][1])
        print("\nunion_find 리스트 :",union_find)
        MST_edge.append(edgeinfo[i])
        print("추가된 MST 간선 :",edgeinfo[i],end="\n\n")
    #서로 root 노드가 같다면 사이클 형성되는 것으로 판단 
    else:
        print("노드",edgeinfo[i][0],"노드",edgeinfo[i][1],"사이클 발생")

costsum = 0           #비용 합 저장 변수
print("\n최종 최소 신장 트리 간선 정보")
for i in range(len(MST_edge)):
    print("노드",MST_edge[i][0],"노드",MST_edge[i][1],"가중치 :",MST_edge[i][2])
    costsum+=MST_edge[i][2]
print("\n최종 비용 :",costsum)