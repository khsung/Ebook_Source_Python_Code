
class Node(object):             #Node 클래스 선언
    def __init__(self, data):   #Node 초기화
        self.data=data          #Node 키 값
        self.prev=None
        self.next=None
        

class DoubleLinkedList(object):  #이중 연결 리스트
                                 #클래스 선언
    def __init__(self):          #리스트 초기화
        self.prev=None           #앞 노드
        self.next=None           #뒤 노드

    def addnode(self,node):      #뒤에 원소 삽입
        if self.next==None:
            self.next=node
        else:
            curr=self
            while curr.next!=None:
                curr=curr.next
            curr.next=node
            node.prev=curr

    def deletenode(self,data):   #특정 원소 제거
        if self.next==None:
            print("공백 리스트")
        else:
            while self.next!=None:
                #다음 노드가 지울 노드일 때
                if self.next.data==data:
                    temp=self.next
                    self.next=self.next.next
                    #다음 노드가 마지막 노드가
                    #아니면 그 다음 노드의
                    #앞 노드를 현재 노드로 연결
                    if self.next!=None:
                        self.next.prev=self
                    del temp
                    return
                self=self.next
        print("해당 노드 없음")

    def printnode(self):         #리스트 출력
        if self.next==None:
            print("공백 리스트")
        else:
            print("이중 연결 리스트 = ",end="")
            while self.next!=None:
                print(self.next.data,end="   ")
                self=self.next
            print()

slist=DoubleLinkedList()   #이중 연결 리스트 생성
slist.printnode()
slist.addnode(Node(10))
slist.addnode(Node(20))
slist.addnode(Node(30))
slist.printnode()
slist.deletenode(2)
slist.deletenode(20)
slist.printnode()
slist.deletenode(30)
slist.printnode()
slist.deletenode(10)
slist.printnode()
