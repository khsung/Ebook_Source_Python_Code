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
        #else:
        #    if curr.left==None and curr.right==None:
        #        if parent==None

    def printnode(self):
        print(self.data)
        print(self.right.data)
        print(self.left.data)
        print(self.left.right.data)


tree=Btree()
tree.insertnode(3)
tree.insertnode(4)
tree.insertnode(1)
tree.insertnode(2)
tree.printnode()
tree.deletenode(100)