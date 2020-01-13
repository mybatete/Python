import sys

def main():
	
	MAXADDR=input("Enter The Size of The Database: ")	

	pList = [None] * MAXADDR

	DIFF=input("Enter The Subtraction Value : ")	

	try:
		fp = open("subtraction-Bank_Acct.txt", "r")

	except IOError:
		sys.exit("\n\n\nUnable to Open File!!!\n\n\n")

	i    = 1
	line = fp.readline()
	while True:
		line = fp.readline()
		if line == "":
			break
		
		line    = line.strip()
		field   = line.split()
		key	= int(field[0])
		address = key - DIFF

		pList[address] = field
		print pList[address]
		print pList[address][0] 
		i = i+1

	i -= 1
	print "Max Entry at Address: ", i
			
	print "\n\nListed Database contains %d Records\n\n" % i  
	

	done = False

	while not done:
		response = raw_input("Exit Records Database? 'Y/N': ")
		if response.upper() == "Y":
			done  = True
		else:

			key     = input("Enter the Key: ")
			address = key - DIFF

			if address < MAXADDR:
				print pList[address]
			else:
				print "\n\nError: Address Exceed Database Range!!!!\n\n"


		
main()
