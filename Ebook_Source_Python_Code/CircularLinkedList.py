
class Node(object):                 #Node 클래스 선언
    def __init__(self, data):       #Node 초기화
        self.data = data            #키 값

class CircularLinkedList(object):   #원형 연결 리스트 클래스 선언
    def __init__(self):             #리스트 초기화
        self.next = None

    def addnode(self, node):        #뒤에 원소삽입
        if self.next == None:       #공백 리스트일 경우
            self.next = node
            node.next = self.next
        else:                       #공백 리스트가 아닐 경우
            curr = self.next
            #가장 끝 노드로 이동
            while curr.next != self.next:
                curr = curr.next
            curr.next = node
            node.next = self.next

    def deletenode(self, data):     #특정 원소제거
        if self.next == None:
            print("공백 리스트")
        else:
            curr = self.next
            #헤드 노드의 다음 노드가 지울 노드일 경우
            if self.next.data == data:
                temp = self.next
                #노드가 한 개일 경우
                if self.next.next == self.next:
                    self.next = None
                    del temp
                    return
                else:
                    #가장 뒤로 이동 후 원형으로 연결
                    while curr.next != self.next:
                        curr = curr.next
                    curr.next = self.next.next
                    self.next = self.next.next
                    del temp
                    return          
            else:
                #지울 노드 탐색
                while curr.next != self.next:
                    if curr.next.data == data:
                        temp = curr.next
                        curr.next = curr.next.next
                        del temp
                        return
                    curr = curr.next
        print("해당 노드 없음")

    def printnode(self):           #리스트 출력
        if self.next == None:
            print("공백 리스트")
        else:
            print("원형 연결 리스트 = ",end="")
            curr = self.next
            print(curr.data,end="   ")
            while self.next != curr.next:
                print(curr.next.data,end="   ")
                curr = curr.next
            print("  다음 노드 =",curr.next.data)
           
slist = CircularLinkedList()     #원형 연결 리스트 생성
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

