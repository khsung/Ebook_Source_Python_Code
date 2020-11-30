
class CircularQueue:          #원형 큐 클래스 선언

    def __init__(self, size):
        self.front=0
        self.rear=0
        self.queuesize=size
        self.data=[None]*size

    def isempty(self):       #원형 큐 공백상태 체크
        if self.front==self.rear:
            return True
        else:
            return False

    def isfull(self):        #원형 큐 포화상태 체크
        if (self.rear+1)%self.queuesize == self.front:
            return True
        else:
            return False

    def enqueue(self, data):  #Rear 위치에 원소 삽입
        if self.isfull()==True:
            print("포화 원형 큐")
        else:
            self.rear=(self.rear+1)%self.queuesize
            self.data[self.rear] = data
        
    def dequeue(self):       #Front 다음 위치 원소 제거
        if self.isempty() == True:
            print("공백 원형 큐")
        else:
            self.front=(self.front+1)%self.queuesize
            
    def peek(self):          #Front 다음 위치 원소 출력
        if self.isempty() == True:
            print("공백 원형 큐")
        else:
            print("첫 번째 원소 : ",self.data
                  [(self.front+1)%self.queuesize])
        
    def printqueue(self):    #원형 큐 출력
        if self.isempty() == True:
            print("공백 원형 큐")
        else:
            f=self.front
            r=self.rear
            print("원형 큐 = ",end="")
            while f%self.queuesize != r%self.queuesize:
                print(self.data[(f+1)%self.queuesize],end="   ")
                f=(f+1)%self.queuesize
            print()
        
cqueue=CircularQueue(4)
cqueue.enqueue(10)
cqueue.enqueue(20)
cqueue.peek()
cqueue.enqueue(30)
cqueue.printqueue()
cqueue.dequeue()
cqueue.peek()
cqueue.enqueue(40)
cqueue.enqueue(50)
cqueue.printqueue()
