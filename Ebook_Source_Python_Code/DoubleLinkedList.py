
class Node(object):                 #Node 클래스 선언
    def __init__(self, data):       #Node 초기화
        self.data = data            #Node 키 값
        self.prev = None
        self.next = None
        
class DoubleLinkedList(object):     #이중 연결 리스트 클래스 선언
    def __init__(self):             #리스트 초기화
        self.prev = None            #앞 노드
        self.next = None            #뒤 노드

    def addnode(self,node):         #뒤에 원소 삽입
        curr = self
        #다음 노드가 없을 때까지 뒤로 이동
        while curr.next != None:
            curr = curr.next
        #노드 연결
        curr.next = node
        node.prev = curr

    def deletenode(self,data):      #특정 원소 제거
        if self.next == None:
            print("공백 리스트")
        else:
            while self.next != None:
                #다음 노드가 지울 노드일 때
                if self.next.data == data:
                    #지울 노드를 임시 저장
                    temp = self.next
                    #지울 노드의 next를 저장
                    self.next = self.next.next
                    #다음 노드가 존재할 경우 양방향 연결
                    if self.next != None:
                        self.next.prev = self
                    del temp
                    return
                self = self.next
        print("해당 노드 없음")

    def printnode(self):            #리스트 출력
        if self.next == None:
            print("공백 리스트")
        else:
            print("이중 연결 리스트 = ",end="")
            while self.next != None:
                print(self.next.data,end="   ")
                self = self.next
            print()

slist = DoubleLinkedList()          #이중 연결 리스트 생성
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
