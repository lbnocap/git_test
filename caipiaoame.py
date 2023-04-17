import random

t1="开始游戏"
t2="结束游戏"
print(t1.center(50,'*'))
data1=[]
money=int(input("请输入投入的金额"))
print("你现在的余额为{}".format(money))
while True:
    for i in range(6):
        n=random.choice([0,1])
        data1.append(n)
    if money<2:
        print("您的余额不足，请充值")
        m=int(input("请输入投入的金额"))
        if int(m)==0:
            break
        else:
            money=int(m)
    while True:
        j=int(input("请输入彩票购买数量"))
        if money-j*2<0:
            print("您的余额不足请充值")
        else:
            money=money-j*2
            print("您现在的余额为:{}".format(money))
            break
    print("中奖数据有六位数，每位数的为0或者1")
    n2=input("请猜测中奖数据：（输入的数字为0或者1）")
    print(str(data1))
    f=[]
    for x in n2:
      f.append(x)
    f1=str(f)
    f2=f1.split("'")
    f3="".join(f2)
    print("你猜测的数据为：",f3)
    if f3==str(data1):
       print("中奖数字为：",data1)
       print("恭喜你，中大奖啦!")
       money=money+j*100
       print("您现在的余额为",money)
    else:
       print("中奖数字为：", data1)
       print("真遗憾，您没有中奖！")
    con = input("请问还要继续么？结束请输入no,继续请任意输入字符：")
    if con=="no":
        break
    data1=[]
print(t2.center(50,"*"))
print("你的余额为：%d元"%money)