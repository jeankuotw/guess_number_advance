#題目：請使用者決定隨機數字的開始值和結束值
#讓使用者重複輸入數字去猜
#如果猜對了,要顯示"你答對了"
#如果猜錯了,要提示比答案 大/小
#並顯示猜的次數

import random #載入模組random

start = input('請決定隨機數字範圍開始值：')
end = input('請決定隨機數字範圍結束值：')
start = int(start) #型別轉換,將字串轉為數字
end = int(start)

r = random.randint(start, end) #使用random模組中的函式(功能)randint(隨機產生整數),數字界在使用者輸入的開始值~結束值的整數
count = 0 #猜的次數

while True:
	keyin = input('請猜數字：') #使用者輸入的內容為字串,括號內記得要用''
	keyin = int(keyin) #型別轉換，將字串轉為整數

	count += 1  #count = count +1 的快寫法

	if keyin == r :
		print('你答對了')
		print('這是你猜的第',count,'次')
		break
	elif keyin > r:
		print('比答案大')
	else:
		print('比答案小')
	print('這是你猜的第',count,'次')
