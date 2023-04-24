def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print("y cant be zero")
    else:
        print("the result is {}".format(result))
    finally:
        print("aaa")
def temp_convert(var):
    try:
        return int(var)
    except (ValueError) as Argument:
        print("参数没有包含数字\n",Argumente)
temp_convert(12.312)
try:
  temp_convert("xyz")
except NameError:
    print("参数输入错误")
