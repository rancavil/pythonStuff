num = input("Number : ")

# generator to create a set of pairs numbers
def genPairsNumbers(x):
	n = 1
	c = 0 
	while n <= int(x):
		if c%2 != 0:
			yield c
			n = n + 1
		c = c + 1
	
def billsq(num):
	if int(num) < 0:
		return -1
	else:
		return sum(genPairsNumbers(num))
	

result = billsq(num)

if result >= 0:
	print("%d ^ 2 = %d \n"%(int(num),result))
else:
	print("Only numbers >= 0")
