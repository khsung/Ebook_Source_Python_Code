
#트리 방문 백트래킹 예제
class Tree(object):
    def __init__(self,data):
        self.data=data

        #방문한 노드인지
        #체크하는 변수
        self.visited=0
        self.Lchild=None
        self.Rchild=None

#def backtrackingFindAnswer(self):


#백트래킹을 위한 예제이므로
#단순한 트리구조 생성
Anode=Tree('A')
Bnode=Tree('B')
Cnode=Tree('C')
Dnode=Tree('D')
answer='D'
Anode.Lchild=Bnode   #   A
Bnode.Lchild=Cnode   #  B
Bnode.Rchild=Dnode   # C D

