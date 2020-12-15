
dic={0:'AAA',1:'BBB',2:'CCC'}
print("딕셔너리 : ",dic)
print(dic.keys())  #키 값 출력
print(dic.values()) #데이터 값 출력

#키 값 1 인 데이터 출력
print("키 값 1인 데이터 :",dic[1])
dic['DDD']=3 #키 값 'DDD'인 데이터 3 추가
del dic[2]   #키 값 2인 데이터 삭제
print("딕셔너리 : ",dic)

