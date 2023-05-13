import time
from functools import wraps
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
def record_time_log(log_time_file="time_log"):
 def record_time(func):
    """自定义装饰函数的装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        log_str= func.__name__+':'+ str(time.time() - start)+'秒'
        print(log_str)
        with open(log_time_file, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_str + '\n')
        
        return result
        
    return wrapper
 return record_time
#插入排序
@record_time_log()
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
print(x)