class Btree(object):
    def __init__(self):
        self.data=None;
        self.left=self.right=None;
    
    def insert(self,data):
        if self.data==None:
            self.data=data
        else:
            if self.data<data:
                if self.right==None:
                    newnode=Btree()
                    self.right=newnode
                    newnode.insert(data)


    def printnode(self):
        print(self.data)
        print(self.right.data)
tree=Btree()
tree.insert(1)
tree.insert(2)
tree.printnode()