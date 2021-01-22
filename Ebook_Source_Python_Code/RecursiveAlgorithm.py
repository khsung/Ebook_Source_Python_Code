
def recursive(num):
    if num==0:    #종료 조건
        print("sum 종료")
        return 0
    else:
        print("num =", num)
        return num+recursive(num-1)

print("총 합 :",recursive(5))

