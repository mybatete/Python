import sys

#MAXADDR=17389
#MAXADDR=224737


def main():
	
	MAXADDR=input("Enter The Size of The Database: ")	

	pList = [None] * MAXADDR

	try:
		fp = open("modulo-DMV.txt", "r")

	except IOError:
		sys.exit("\n\n\nUnable to Open File!!!\n\n\n")

	i          = 0
	collisions = 0
	probes     = 0
	line       = fp.readline()
	while True:
		line = fp.readline()
		if line == "":
			break
		
		line    = line.strip()
		field   = line.split()
		skey	= field[1]
		key	= int(skey[0]+skey[2]+skey[4]+skey[6]+skey[0])
		address = key

		if pList[address] != None:
			collisions += 1	

		while pList[address] != None and address < MAXADDR:
			probes  += 1	
			address += 1
			#print "Collision for Key %d at Address: %d" % (key, address)

		if pList[address] != None or address >= MAXADDR:
			print "Collision Unresolved for Key %d. Last Address: %d" % (key, address)
			exit()
		else:

			pList[address] = field
			print pList[address]
			#print pList[address][0] 
			i = i+1

	#print "Max Entry at Address: ", i
			
	print "\n\nListed Database contains %d Records" % i  
	print "\nNumber of Collision Instances: %d" % collisions	
	print "\nNumber of Probing Instances: %d\n\n" % probes	

	done = False

	LEN=len(skey)
	while not done:
		response = raw_input("Exit Records Database? 'Y/N': ")
		if response.upper() == "Y":
			done  = True
		else:

			skey     = raw_input("Enter the Key: ")
			
			if(len(skey)== LEN):
				key	= int(skey[0]+skey[2]+skey[4]+skey[6]+skey[8])
				address = key


				while pList[address][1] != skey and address < MAXADDR:
					address    += 1
					print "Skipping Collision for Key %d at Address: %d" % (key, address)
	
				if pList[address][1] != skey or address >= MAXADDR:
					print "Collision Unresolved for Key %d. Last Address: %d" % (key, address)
					print "\n\nRecord Not On File!!!\n\n"
					exit()
				else:
					print pList[address]

			else:
				print "\n\nInvalid Key: %s\n\n", skey

		
main()
