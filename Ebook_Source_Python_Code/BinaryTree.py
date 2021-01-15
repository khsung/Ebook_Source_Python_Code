
class Btree(object):
    #데이터와 두 자식노드 초기화
    def __init__(self):
        self.data = None
        self.left = self.right = None

    #노드 삽입
    def insertnode(self,data):
        #현재노드가 비어있을 경우
        if self.data == None:
            self.data = data
        else:
            #현재 노드 데이터보다 클 때
            if self.data < data:
                #오른쪽 자식이 없을 경우 삽입
                if self.right == None:
                    newnode = Btree()
                    self.right = newnode
                    newnode.insertnode(data)

                #오른쪽 자식이 있을 경우 이동
                else:
                    self = self.right
                    self.insertnode(data)

            #현재 노드 데이터보다 같거나 작을 때
            else:
                #왼쪽 자식이 비어있을 경우 삽입
                if self.left == None:
                    newnode = Btree()
                    self.left = newnode
                    newnode.insertnode(data)
                    self.parent = newnode
                #왼쪽 자식이 있을 경우 이동
                else:
                    self = self.left
                    self.insertnode(data)

    #노드 삭제
    def deletenode(self,data):
        #현재 노드의 부모노드를 저장하기 위한 전역변수
        global parent

        #루트노드가 비어있을 경우 오류 출력
        if tree.data == None:
            print("공백 이진 트리")

        #현재 노드의 데이터보다 삭제할 데이터가 클 경우
        elif self.data < data:
            #오른쪽 자식이 없을 경우 오류출력
            if self.right == None:
                print(data,"에 해당하는 원소 없음\n")

            #현재 노드를 부모노드로 저장하고
            #오른쪽 자식으로 이동
            else:
                parent = self
                self = self.right
                self.deletenode(data)

        #현재 노드의 데이터보다 삭제할 데이터가 작을 경우
        elif self.data > data:
            #왼쪽 자식이 없을 경우 오류출력
            if self.left == None:
                print(data,"에 해당하는 원소 없음\n")
            
            #현재 노드를 부모노드로 저장하고
            #오른쪽 자식으로 이동
            else:
                parent = self
                self = self.left
                self.deletenode(data)

        #현재 노드가 지워야 할 노드일 경우
        else:
            #자식노드가 없을 경우
            if self.left == None and self.right == None:
                #부모의 오른쪽 자식노드가 현재 노드일 경우
                #부모의 오른쪽 자식노드 연결을 끊어줌
                if parent.right == self:
                    parent.right = None

                #부모의 왼쪽 자식노드가 현재 노드일 경우
                #부모의 왼쪽 자식노드 연결을 끊어줌
                elif parent.left == self:
                    parent.left = None

                #둘다 아닐 경우는 루트 노드밖에없음
                #따라서 노드삭제가 아닌 데이터만 삭제
                else:
                    self.data = None

            #오른쪽 자식만 있을 경우 지울 노드를 임시 저장한 뒤
            #오른쪽 자식으로 이동 후 왼쪽 자식 노드가 없을 때까지
            #왼쪽 자식 노드로 이동하면 지울 노드의 키 값보다
            #큰 값 중 가장 작은 값을 구할 수 있다
            #해당 값을 원래 지울 노드의 키 값으로 저장하고
            #해제하면 트리 구조를 유지할 수 있다
            elif self.left == None:
                temp = self
                parent = self
                self = self.right
                
                while self.left != None:
                    parent = self
                    self = self.left
                temp.data,self.data = self.data,temp.data
                parent.left = None
                del(self)

            #지울 노드를 임시 저장한 뒤 왼쪽 자식으로 이동 후
            #오른쪽 자식 노드가 없을 때까지 오른쪽 자식 노드로
            #이동하면 지울 노드의 키 값보다 작은 값 중
            #가장 큰 값을 구할 수 있다
            #해당 값을 원래 지울 노드의 키 값으로 저장하고
            #해제하면 트리 구조를 유지할 수 있다
            else:
                temp = self
                parent = self
                self = self.left
                while self.right != None:
                    parent = self
                    self = self.right
                temp.data,self.data = self.data,temp.data
                parent.right = None
                del(self)

    #전위 순회 root->left->right
    def preorder(self):
        def preorder(node):
            if node == None:
                return
            else:
                print(node.data,end="  ")       #root 출력
                preorder(node.left)             #left 이동
                preorder(node.right)            #right 이동

        if tree.data == None:
                print("공백 이진 트리")
        else:
            print("전위 순회 : ",end="")
            if self == None:
                return
            else:
                print(self.data,end="  ")       #root 출력
                preorder(self.left)             #left 이동
                preorder(self.right)            #right 이동
        print()

    #중위 순회 left->root->right
    def inorder(self):
        def inorder(node):
            if node == None:
                return
            else:
                inorder(node.left)              #left 이동
                print(node.data,end="  ")       #root 출력
                inorder(node.right)             #right 이동

        if tree.data == None:
                print("공백 이진 트리")
        else:
            print("중위 순회 : ",end="")
            if self == None:
                return
            else:
                inorder(self.left)              #left 이동
                print(self.data,end="  ")       #root 출력
                inorder(self.right)             #right 이동
        print()
          
    #후위 순회 left->right->root
    def postorder(self):
        def postorder(node):
            if node == None:
                return
            else:
                postorder(node.left)            #left 이동
                postorder(node.right)           #right 이동
                print(node.data,end="  ")       #root 출력

        if tree.data == None:
                print("공백 이진 트리")
        else:
            print("후위 순회 : ",end="")
            if self == None:
                return
            else:
                postorder(self.left)            #left 이동
                postorder(self.right)           #right 이동
                print(self.data,end="  ")       #root 출력
        print()

tree = Btree()
parent = Btree()
tree.preorder()    #공백 상태 순회시도
tree.insertnode(3)
tree.insertnode(1)
tree.insertnode(5)
tree.insertnode(0)
tree.insertnode(2)
tree.insertnode(4)
tree.insertnode(6)
tree.deletenode(10)  #없는 노드 삭제 시도
tree.insertnode(10)
tree.deletenode(10)

tree.preorder()
tree.inorder()
tree.postorder()
