prime=True
num = input("Enter a Number: ")

if num <1:
	print "Enter a Number Greater Than 1!!!"
	exit()

for k in xrange(2,num):
	if num % k == 0:
		prime = False
		break

if prime == True:
	print num,"is a Prime Number"
else:
	print num,"is NOT a Prime Number"

