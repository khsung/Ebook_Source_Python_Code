class Btree(object):
    def __init__(self):
        self.data=None;
        self.left=self.right=None;
    def insertnode(self,data):
        if self.data==None:
            self.data=data
        else:
            if self.data<data:
                if self.right==None:
                    newnode=Btree()
                    self.right=newnode
                    newnode.insertnode(data)
                else:
                    self=self.right
                    self.insertnode(data)
            else:
                if self.left==None:
                    newnode=Btree()
                    self.left=newnode
                    newnode.insertnode(data)
                else:
                    self=self.left
                    self.insertnode(data)

    def deletenode(self,data):
        if tree.data==None:
            print("공백 이진 트리")
        elif self.data<data:
            if self.right==None:
                print(data,"에 해당하는 원소 없음")
            else:
                parent=self
                self=self.right
                self.deletenode(data)
        elif self.data>data:
            if self.left==None:
                print(data,"에 해당하는 원소 없음")
            else:
                parent=self
                self=self.left
                self.deletenode(data)
        else:
            if self.left==None and self.right==None:
                if parent.right==self:
                    parent.right=None
                elif parent.left==self:
                    parent.left=None
                else:
                    self.data=None;
            elif self.left==None:
                temp=self
                parent=self
                self=self.right
                if self.left==None:
                    temp.data,self.data=self.data,temp.data
                    parent.right=None
                    del(self)
                else:
                    while self.left!=None:
                        parent=self
                        self=self.left
                    temp.data,self.data=self.data,temp.data
                    parent.left=None
                    del(self)
            else:
                temp=self
                parent=self
                self=self.left
                if self.right==None:
                    temp.data,self.data=self.data,temp.data
                    parent.left=None
                    del(self)
                else:
                    while self.right!=None:
                        parent=self
                        self=self.right
                    temp.data,self.data=self.data,temp.data
                    parent.right=None
                    del(self)

    def preorder(self):
        def preorder(node):
            if node==None:
                return
            else:
                print(node.data,end="  ")
                preorder(node.left)
                preorder(node.right)

        if tree.data==None:
                print("공백 이진 트리")
        else:
            print("전위 순회 : ",end="")
            if self==None:
                return
            else:
                print(self.data,end="  ")
                preorder(self.left)
                preorder(self.right)
        print()

    def inorder(self):
        def inorder(node):
            if node==None:
                return
            else:
                inorder(node.left)
                print(node.data,end="  ")
                inorder(node.right)

        if tree.data==None:
                print("공백 이진 트리")
        else:
            print("중위 순회 : ",end="")
            if self==None:
                return
            else:
                inorder(self.left)
                print(self.data,end="  ")
                inorder(self.right)
        print()
            
    def postorder(self):
        def postorder(node):
            if node==None:
                return
            else:
                postorder(node.left)
                postorder(node.right)
                print(node.data,end="  ")

        if tree.data==None:
                print("공백 이진 트리")
        else:
            print("후위 순회 : ",end="")
            if self==None:
                return
            else:
                postorder(self.left)
                postorder(self.right)
                print(self.data,end="  ")
        print()

tree=Btree()
parent=Btree()
tree.preorder()
tree.insertnode(3)
tree.insertnode(1)
tree.insertnode(5)
tree.deletenode(5)
tree.insertnode(0)
tree.deletenode(0)
tree.insertnode(2)
tree.insertnode(4)
tree.insertnode(6)
#tree.insertnode(10)
#tree.deletenode(10)
#tree.deletenode(100)
tree.preorder()
tree.inorder()
tree.postorder()
