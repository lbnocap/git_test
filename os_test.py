
import os, sys

# 打开文件
fd = os.open("test.txt",os.O_APPEND|os.O_RDWR)

# 写入字符串
os.lseek(fd,0,0)
ret = os.write(fd,str.encode("换行"+"\n"))

# 输入返回值
print ("写入的位数为: ")
print  (ret)

print ("写入成功")

# 关闭文件
os.close(fd)
print ("关闭文件成             功!!")