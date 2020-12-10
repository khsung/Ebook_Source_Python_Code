
def recursive(num):
    if num==0:    #종료 조건
        print("count 종료")
        return 0
    else:
        print("count =",num)
        return num+recursive(num-1)

print("총 걸린 시간 :",recursive(5))

