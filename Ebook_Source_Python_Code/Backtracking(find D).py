
#트리 방문 백트래킹 예제
class Tree(object):
    def __init__(self,data):
        self.data = data
        self.visited = 0        #방문한 노드인지 체크하는 변수
        self.Lchild = None      #왼쪽 자식 노드
        self.Rchild = None      #오른쪽 자식 노드

#원하는 원소를 찾기 위해 왼쪽 자식부터 탐색
#재귀 알고리즘으로 구현한 깊이 우선 탐색
def backtrackingFindAnswer(self):
    print("현재 노드의 데이터 : " + self.data)
    if self.data == answer:
        print("데이터 " + self.data + " 찾음")
    else:
        #왼쪽 자식노드를 방문 안 했을 경우 왼쪽 자식으로 이동
        if self.Lchild != None and self.Lchild.visited == 0:
            backtrackingFindAnswer(self.Lchild)
        #오른쪽 자식노드를 방문 안 했을 경우 오른쪽 자식으로 이동
        if self.Rchild != None and self.Rchild.visited == 0:
            backtrackingFindAnswer(self.Rchild)
        #현재 노드를 방문한 노드로 처리
        self.visited = 1

#백트래킹을 위한 예제이므로 단순한 트리구조 생성
Anode = Tree('A')
Bnode = Tree('B')
Cnode = Tree('C')
Dnode = Tree('D')

answer = 'D'
Anode.Lchild = Bnode   #   A
Bnode.Lchild = Cnode   #  B
Bnode.Rchild = Dnode   # C D
backtrackingFindAnswer(Anode)
