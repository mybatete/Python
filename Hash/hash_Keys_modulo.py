import sys

MAXADDR=224737

def main():
	
	#MAXADDR=input("Enter Large Prime Number Greater Than Max Address : ")	

	pList = [None] * MAXADDR

	try:
		fp = open("modulo-DMV.txt", "r")

	except IOError:
		sys.exit("\n\n\nUnable to Open File!!!\n\n\n")

	i    = 0
	line = fp.readline()
	while True:
		line = fp.readline()
		if line == "":
			break
		
		line    = line.strip()
		field   = line.split()
		key	= int(field[1])
		address = key % MAXADDR

		pList[address] = field
		print pList[address]
		print pList[address][0] 
		i = i+1

	#print "Max Entry at Address: ", i
			
	print "\n\nListed Database contains %d Records\n\n" % i  
	

	done = False

	while not done:
		response = raw_input("Exit Records Database? 'Y/N': ")
		if response.upper() == "Y":
			done  = True
		else:

			key     = input("Enter the Key: ")
			address = key % MAXADDR

			if address < MAXADDR:
				print pList[address]
			else:
				print "\n\nError: Address Exceed Database Range!!!!\n\n"


		
main()
