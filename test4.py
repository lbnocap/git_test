while True:
    try:
     age=int(input("请输入你家狗的年龄："))
     print(" ")
     if age<=0:
        print("fucking kining me")
        print("  ")
     elif age==1:
        print("相当于人的14岁")
        break
     elif age==2:
        print("相当与人的22岁")
        break
     elif age>2:
        human=22+(age-2)*5
        print("对应人的年龄:",human)
        break
    except ValueError:
      print("输入不合法")

