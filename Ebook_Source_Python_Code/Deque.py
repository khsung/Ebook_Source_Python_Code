
class Deque:        #Deque 클래스 선언
    def __init__(self):   #Deque 배열로 초기화
        self.data=[]
        
    def isempty(self):   #Deque 공백확인
        return not self.data
    
    def frontenQ(self, data):   #앞에 원소 삽입
        self.data.insert(0, data)

    def rearenQ(self, data):    #뒤에 원소 삽입
        self.data.append(data)
        
    def frontdeQ(self):       #앞 원소 제거
        if self.isempty()==True:
            print("공백 큐")
        else:
            self.data.pop(0)
            
    def reardeQ(self):       #뒤 원소 제거
        if self.isempty()==True:
            print("공백 큐")
        else:
            self.data.pop()
            
    def printdeque(self):    #Deque 출력
        print(self.data)
    
deque=Deque()
deque.reardeQ()
deque.rearenQ(10)
deque.frontenQ(20)
deque.rearenQ(30)
deque.printdeque()
deque.frontdeQ()
deque.printdeque()
deque.reardeQ()
deque.printdeque()

