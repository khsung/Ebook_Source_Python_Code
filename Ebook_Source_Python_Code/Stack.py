
class Stack(list):   #스택 클래스 선언
    def __init__(self):   #스택 리스트로 초기화
        self.data=[]

    def isempty(self):    #스택 공백 상태 체크
        return not self.data

    def push(self, data):  #리스트 뒤에 원소 삽입
        self.data.append(data)

    def pop(self):     #리스트 뒤 원소 제거
        if self.isempty()==True:
            print("공백 스택")
        else:
            self.data.pop()

    def printstack(self):  #스택 출력
        print(self.data)

stack=Stack()
stack.pop()
stack.push(10)
stack.push(20)
stack.printstack()
stack.pop()
stack.printstack()