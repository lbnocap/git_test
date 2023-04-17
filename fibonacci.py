#fib是计算N个斐波那契数列
print("该模块被引用或执行")
if __name__=='__main__':
    print("只在本模块中运行")
def fib(n):
    a,b=0,1
    counter=0
    result=[]
    while counter<n:
        result.append(b)
        a,b=b,a+b
        counter+=1
    return  result
#fib2是打印到max的数列
def fib2(max):
    a,b=0,1
    while b<max:
        print(b,end=" ")
        a,b=b,a+b
    return
fib2(500)


