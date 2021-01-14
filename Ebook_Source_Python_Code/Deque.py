
class Deque:                    #Deque 클래스 선언
    def __init__(self):         #Deque 배열로 초기화
        self.data=[]
        
    def isempty(self):          #Deque 공백확인
        return not self.data
    
    def enqueueF(self, data):   #앞에 원소 삽입
        self.data.insert(0, data)

    def enqueueR(self, data):   #뒤에 원소 삽입
        self.data.append(data)
        
    def dequeueF(self):         #앞 원소 제거
        if self.isempty()==True:
            print("공백 큐")
        else:
            self.data.pop(0)
            
    def dequeueR(self):         #뒤 원소 제거
        if self.isempty()==True:
            print("공백 큐")
        else:
            self.data.pop()
            
    def printdeque(self):       #Deque 출력
        print(self.data)
    
deque=Deque()                   #데크 생성
deque.dequeueR()
deque.enqueueR(10)
deque.enqueueF(20)
deque.enqueueR(30)
deque.printdeque()
deque.dequeueF()
deque.printdeque()
deque.dequeueR()
deque.printdeque()

