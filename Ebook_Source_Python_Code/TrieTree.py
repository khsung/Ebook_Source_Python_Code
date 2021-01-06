
class trie(object):
    def __init__(self):
        #알파벳 개수 만큼 None으로 배열 초기화 0번은 a, 25번은 z
        self.next = [None for i in range(26)]

    #Trie 구조 만들기
    def maketrie(self,wordset,currword,currwordindex):
        #wordset의 문자열 개수만큼 반복
        while currword < len(wordset):
            #현재노드를 초기 노드로 초기화
            currnode = self

            #각 문자열의 크기만큼 반복
            while currwordindex < len(wordset[currword]):
                #해당 문자의 인덱스 배열이 None일 때 trie클래스 생성하고 연결
                #ord는 문자의 아스키 코드값을 반환해주는 파이썬의 내장 함수
                if currnode.next[ord(wordset[currword][currwordindex]) - ord('a')] == None:
                    currnode.next[ord(wordset[currword][currwordindex]) - ord('a')] = trie()
                    currnode = currnode.next[ord(wordset[currword][currwordindex]) - ord('a')]
                #해당 문자의 인덱스 배열에 trie클래스가 있을 때(이미 생성된 노드일 때)
                else:
                    currnode = currnode.next[ord(wordset[currword][currwordindex]) - ord('a')]
                currwordindex+=1

            #다음 문자열의 첫번째 인덱스로 넘어감
            currword+=1
            currwordindex = 0
    
    #문자열 찾는 함수
    def findword(self,word):
        check = True          #존재하는지 체크하는 변수
        currwordindex = 0
        curr = self
        #단어의 길이만큼 반복
        while(currwordindex < len(word)):
            #해당 문자에 해당하는 인덱스가 노드로 연결되어 있지 않을 때
            #존재하지 않는 것으로 판단
            if curr.next[ord(word[currwordindex]) - ord('a')] == None:
                check = False
                break
            #다음 노드로 이동
            else:
                curr = curr.next[ord(word[currwordindex]) - ord('a')]
                currwordindex+=1
        if check == True:
            print(word,"는 존재하는 문자열",end="\n\n")
        else:
            print(word,"는 존재하지 않는 문자열",end="\n\n")

#Trie에 저장할 문자열
wordset = ["tree","trie","trim","steel","stack","bind","bin"]
#몇 번째 단어인지를 뜻하는 변수
currword = 0
#각 단어의 인덱스 의미
currwordindex = 0
root = trie()
root.maketrie(wordset,currword,currwordindex)

for i in range(3):
    word = input("찾을 문자열 입력 : ")
    root.findword(word)
