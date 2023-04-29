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
#插入排序
def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
x=[4,5,48,78,74,85,74,87,84,85,45,48,74,987,6,74,968,74,85]
print(insertionsort(x))



