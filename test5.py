print('二、数字猜谜游戏')
print('数字猜谜游戏！')

a = 1
i = 0
while a == 20:
   a = int (input ('请输入你猜的数字：'))
   i += 1
   if a == 20:
      if i<3:
         print('真厉害，这么快就猜对了！')
      else :
         print('总算猜对了，恭喜恭喜！')
   elif a < 20:
      print('你猜的数字小了，不要灰心，继续努力！')
   else :
      print('你猜的数字大了，不要灰心，继续加油！')