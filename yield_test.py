import fibonacci
import time
a=fibonacci.fib(10)
print(a)
print("输入1开始计时，CTRL+C停止计时")
T=input(":")
while T:
    print("\n")
    starttime=time.time()
    try:
        while True:
            print("计时：",round(time.time()-starttime,0),"秒")
            time.sleep(2)
    except KeyboardInterrupt:
        print("结束")
        endtime=time.time()
        print("总共耗费时间为：",round(endtime-starttime,2),"secs")
        break


