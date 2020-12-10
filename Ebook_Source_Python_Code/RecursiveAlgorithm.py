
def recursive(num):
    if num==0:
        print("count 종료")
    else:
        print("count =",num)
        recursive(num-1)

recursive(5)

