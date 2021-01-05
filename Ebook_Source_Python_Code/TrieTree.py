
class trie(object):
    def __init__(self,wordset,currword,currwordindex):
        self.next = [None for i in range(26)]

    def
        #init으로하니 무한 반복됨 함수를 끊어서 작성해야할듯
        while currword<len(wordset):
            currnode=self
            while currwordindex<len(wordset[currword]):
                if currnode.next[ord(wordset[currword][currwordindex])-ord('a')]==None:
                    currnode.next[ord(wordset[currword][currwordindex])-ord('a')]=
                else:

                currwordindex+=1
            currword+=1
            currwordindex=0
    

def findword(trie,word):
    return

wordset = ["tree","trie","trim","steel","stack","bind","bin"]
currword = 0
currwordindex = 0
root = trie(wordset,currword,currwordindex)

#for i in range(3):
#    word=input("찾을 문자열 입력 : ")
#    findword(trie,word)
