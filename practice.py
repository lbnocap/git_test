'''num=int(input("请输入一个整数"))
if num>1:
    try:
        i=2
        while i<num:
            if(num%i==0):
                print("{}不是zhishu".format(num))
                break
            i+=1
        else:
            print("{}是质数".format(num))
    except ValueErro:
        print("输入的值不是整数")
    except:
        print("unexcept error")
else:
    print("0")'''
lower=int(input("请输入一个最小值:"))
upper=int(input("请输入一个最大值:"))
for num in range(lower,upper+1):
    if num>1:
     try:
        i=2
        while i<num:
            if(num%i==0):
                print("{}不是质数".format(num))
                break
            i+=1
        else:
            print("{}是质数".format(num))
     except ValueErro:
        print("输入的值不是整数")
     except:
        print("unexcept error")
else:
    print("exit")


              