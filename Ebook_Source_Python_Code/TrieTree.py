
class trie(object):
    def __init__(self):
        #알파벳 개수 만큼 None으로 배열 초기화 0번은 a, 25번은 z
        self.next = [None for i in range(26)]

    #Trie 구조 만들기
    def maketrie(self,wordset,currword,currwordindex):
        while currword < len(wordset):
            currnode = self
            while currwordindex < len(wordset[currword]):
                if currnode.next[ord(wordset[currword][currwordindex]) - ord('a')] == None:
                    currnode.next[ord(wordset[currword][currwordindex]) - ord('a')] = trie()
                    currnode = currnode.next[ord(wordset[currword][currwordindex]) - ord('a')]
                else:
                    currnode = currnode.next[ord(wordset[currword][currwordindex]) - ord('a')]
                currwordindex+=1
            currword+=1
            currwordindex = 0
    
    def findword(self,word):
        check = True
        currwordindex = 0
        curr = self
        while(currwordindex < len(word)):
            if curr.next[ord(word[currwordindex]) - ord('a')] == None:
                check = False
                break
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
