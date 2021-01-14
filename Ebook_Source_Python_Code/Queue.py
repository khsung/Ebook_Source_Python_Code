
class Queue(list):              #큐 클래스 선언
    def __init__(self):         #큐 리스트로 초기화
        self.data=[]

    def isempty(self):          #큐 공백 상태 체크
        return not self.data

    def enqueue(self, data):    #리스트 뒤에 원소 삽입
        self.data.append(data)

    def dequeue(self):          #리스트 앞 원소 제거
        if self.isempty()==True:
            print("공백 큐")
        else:
            print("Front 원소 제거 :",end="")
            print(self.data.pop(0))

    def printqueue(self):       #큐 출력
        print(self.data)

queue=Queue()
queue.dequeue()
queue.enqueue(10)
queue.enqueue(20)
queue.printqueue()
queue.dequeue()
queue.printqueue()
