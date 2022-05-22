import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input ('請輸入你要猜的數字 ')
	num = int(num)
	if num > r :
		print ('你猜的數字太大了，再猜猜')
	elif num < r:
		print ('你猜的數字太小了，再猜猜')
	else :
		print ('恭喜你猜對了！')
		print ('你已經猜了', count,'次')
		break
	print ('你已經猜了', count,'次')			