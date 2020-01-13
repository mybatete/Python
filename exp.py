
import math

THRESH=21

def main():

	x=input("Enter the value of X: ")

	result = Exp(x)

	print "exp(",x,") =", result


def Exp(num):

	result=0

	for i in xrange(THRESH):

		result += float(math.pow(num,i)) / math.factorial(i)

	return result

main()


