
class Node(object):             #Node 클래스 선언
    def __init__(self, data):   #Node 초기화
        self.data = data
        self.next = None

class SingleLinkedList(object):  #단일 연결 리스트
                                 #클래스 선언
    def __init__(self):       
        self.data = None         #리스트 초기화
        self.next = None

    def addnode(self,node):      #뒤에 원소 삽입
        if self.next == None:
            self.next = node
        else:
            curr = self
            while curr.next != None:
                curr = curr.next
            curr.next = node

    def deletenode(self,data):   #특정 원소 제거
        if self.next == None:
            print("공백 리스트")
        else:
            while self.next != None:
                #다음 노드가 지울 노드일 경우
                #현재노드와 다음 노드의 다음 노드를
                #연결시키고 다음 노드를 해제함
                if self.next.data == data:
                    temp = self.next
                    self.next = self.next.next
                    del temp
                    return
                self = self.next
        print("해당 노드 없음")

    def printnode(self):         #리스트 출력
        if self.next == None:
            print("공백 리스트")
        else:
            print("단일 연결 리스트 = ",end="")
            while self.next != None:
                print(self.next.data,end="   ")
                self = self.next
            print()

slist = SingleLinkedList()    #단일 연결 리스트 생성
slist.printnode()
slist.addnode(Node(10))
slist.addnode(Node(20))
slist.addnode(Node(30))
slist.printnode()
slist.deletenode(2)
slist.deletenode(20)
slist.printnode()
slist.deletenode(10)
slist.printnode()
slist.deletenode(30)
slist.printnode()
