def main():

	x=input("Base: ")
	y=input("Power: ")

	z = power(x,y)	

	print "Result: ", z

def power(x,y):

	result = 1
	count  = 0

	while count < y:
		result *= x
		count  += 1	

	return result


"""
def power(x,y):

	result = 1

	for count in range(y):
		result *= x	

	return result
"""


main()
	
