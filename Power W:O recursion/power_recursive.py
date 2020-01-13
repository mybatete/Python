def main():

	x=input("Base: ")
	y=input("Power: ")

	z = power(x,y)	

	print "Result: ", z

def power(x,y):

	print x,y
	
	if y == 0:
		return 1
	elif y == 1:
		return x
	elif y % 2 == 0:
		return power(x*x, y/2)

	elif y % 2 == 1:
		return power(x*x, y/2) * x


main()
	
