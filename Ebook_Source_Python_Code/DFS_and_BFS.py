
#파이썬은 리스트함수를 제공하기 때문에
#append, pop으로 스택과 큐의 역할을 대신한다

#깊이 우선 탐색
def DFS(graph, visited, startnode, stack):
    #시작 노드 추가
    stack.append(startnode)
    visited[startnode] = 1

    #stack 리스트의 크기가 0이 될 때까지
    while len(stack) > 0:
        #stack 리스트의 마지막 원소를 제거하면서 반환
        printnode = stack.pop()
        print(printnode,end=" ")
        for i in range(len(graph[printnode])):
            #반환한 노드의 인접노드가 방문하지 않은 노드일 경우
            #stack 리스트에 추가
            if graph[printnode][i] == 1 and visited[i] != 1:
                stack.append(i)
                visited[i] = 1
    print()

#너비 우선 탐색
def BFS(graph, visited, startnode, queue):
    #시작 노드 추가
    queue.append(startnode)
    visited[startnode] = 1

    #queue 리스트의 크기가 0이 될 때까지
    while len(queue) > 0:
        #queue 리스트의 첫번째 원소를 제거하면서 반환
        printnode = queue.pop(0)
        print(printnode,end=" ")
        for i in range(len(graph[printnode])):
            #반환한 노드의 인접노드가 방문하지 않은 노드일 경우
            #queue 리스트에 추가
            if graph[printnode][i] == 1 and visited[i] != 1:
                queue.append(i)
                visited[i] = 1
    print()

#그래프 행렬
graph = [[0,1,1,0,0],[1,0,0,1,1],[1,0,0,1,0],[0,1,1,0,0],[0,1,0,0,0]]
#시작 노드
startnode = 0
stack=[]
queue=[]

#그래프 행렬 출력
print("그래프 행렬")
for i in range(len(graph)):
    print(graph[i])

#방문한 노드 체크 리스트 선언
visited = [0,0,0,0,0]
print("\nDFS 순서 : ",end="")
DFS(graph, visited, startnode, stack)

#방문한 노드 체크 리스트 초기화
visited = [0,0,0,0,0]
print("\nBFS 순서 : ",end="")
BFS(graph, visited, startnode, queue)