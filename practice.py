'''lower=int(input("请输入一个最小值:")) #质数练习
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
lower=int(input("请输入一个最小值:")) #阿姆斯特朗数练习
upper=int(input("请输入一个最大值:"))
for num in range(lower,upper+1):
  sum1=0
  temp=num
  n=len(str(num))
  while temp>0:
    digi=temp%10
    sum1+=digi**n
    temp=temp//10
  if sum1==num:
    print("{}is amusitelangshu".format(num))'''
'''
def hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if x%i==0 and y%i==0:
            hcf=i
    return hcf
num1=int(input("min :"))
num2=int(input("max :"))
print(hcf(num1, num2))
 
with open("123.txt","wt") as out_file:
    out_file.write("this is  a os write\n can you see me ")

with open("123.txt","r") as in_file:
    text=in_file.read()
print(text)'''

people={}
for i in range(1,31):
    people[i]=1
index=0
print(people)
i,j=1,0
while i<=31:
    if i==31:
        i=1
    elif j==15:
        break
    else:
        if people[i]==0:
            i+=1
            continue
        else:
         index+=1
         if index==7:
            people[i]=0
            index=0
            print("{}号下船了".format(i))
            j+=1
         else:
            i+=1
            continue


        
              