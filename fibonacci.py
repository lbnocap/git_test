#fib是计算N个斐波那契数列
print("该模块被引用或执行")
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
#五人分yu
def fish1():
    fish=1
    while True:
        tatol,enough=fish,True
        for _ in range(5):
            if (tatol-1)%5==0:
                tatol=(tatol-1)//5*4
            else:
                enough=False
                break
        if enough:
            print("{}条鱼被吊上".format(fish))
            break
        fish+=1 
def main():
    fish = 1
    while True:
        total, enough = fish, True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1)  //  5 * 4
            else:
                enough = False
                break
        if enough:
            print(f'总共有{fish}条鱼')
            break
        fish += 1
if __name__=='__main__':
    print("只在本模块中运行")
    fish1()
    main()
    

