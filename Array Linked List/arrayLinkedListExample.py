from orderedList import orderedList

fp = open("Data_Readings.dat","r")

HashTable=[]

NUM=10000

print "\n\nCreating Hash Table ....\n\n"

#Create a hash tabe containing 10000 linked Lists
for i in xrange(NUM):

	temp = orderedList()

	HashTable.append(temp)

print HashTable

#Read data file:
while True:

	line = fp.readline()

	if line == "":
		break

	line  = line.strip()
	word  = line.split()
	value = int(word[0])

	#Generate a key address using the modulo scheme:
	key   = value % NUM

	#Insert data into linked list using the key
	HashTable[key].add(value)


for i in xrange(NUM):

	HashTable[i].traversal()

print 

value = 549689997
key   = value % NUM

HashTable[key].search(value)

exit()

HashTable[0].traversal()
HashTable[0].search(549689997)

HashTable[1].add(15)
HashTable[1].add(16)
HashTable[1].add(17)

HashTable[1].traversal()
HashTable[2].traversal()


