import util
import time
import random

def play():
  util.clear()
  util.cbc_print("\nLet's us get stared\n")
  for i in range(4):
    print('出題中' + (i%4+1)*'.' + '   ', end='\r')
    time.sleep(1)
  ans = []
  i = 1
  while i<=4:
    tmp = random.randint(0, 9)
    flag = 1
    for num in ans:
      if tmp == num:
        flag = 0
        break
    if flag:
        ans.append(tmp)
        i+=1
  print("放馬過來吧，區區coder，不足為奇")
  count = 0
  final = 0
  while count<8:
    if count == 7:
      print("剩最後一次囉，我可不會同情你的歐\n")
    arr = input("請猜4個數字（各為0~9, 數字間不能重複） : ")
    your_ans = []
    for chr in arr:
      your_ans.append(int(chr))
    a = 0
    b = 0
    for num1 in range(4):
      for num2 in range(4):
        if ans[num1] == your_ans[num2] and num1 == num2:
          a+=1
          break
        elif ans[num1] == your_ans[num2]:
          b+=1
          break
    if a == 4:
      final = 1
      break
    util.cbc_print(f"你得到 {a}A{b}B\n")
    count+=1
  if final:
    util.cbc_print("\n竟然...好啦，至少你讓我獲得快樂，我這就給你最終解答吧，下次不會讓你贏的!!!!\n")
    util.cbc_print("\n!!!I LOVE SITCON HACKATHON 2024!!!\n\n")
    return 1
  else:
    util.cbc_print("哈，太菜了，下次再來吧 ( ´∀`)\n")
    return 0
    