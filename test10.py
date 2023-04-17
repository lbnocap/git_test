#python 冒泡排序
import fibonacci
def maopao(x):
    for i in range(len(x)-1):
        for j in range(len(x)-1-i):
            if x[j]>x[j+1]:
                max1=x[j]
                x[j]=x[j+1]
                x[j+1]=max1
            else:
                max1=x[j+1]
    print(x)
maopao([100,65,858,645,41,852,84,6,1,68,6])
fibonacci.fib2(500)