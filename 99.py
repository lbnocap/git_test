#外边一层循环控制行数
#i是行数
import  fibonacci
import support
import sys
'''i=1
while i<=9:
     #里面一层循环控制每一行中的列数
     j=1
     while j<=i:
          mut =j*i
          print("%d*%d=%d"%(j,i,mut), end="  ")
          j+=1
     print("")
     i+=1'''
for i in range(1,10):
    for j in range(1,i+1):
         mut = i*j
         print("{}*{}={}".format(j,i,mut),end=" ")
    print(" ")
support.print_func("liubo")
x=fibonacci.fib(10)
print(x)
print(dir(fibonacci))