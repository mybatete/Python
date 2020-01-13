fp=open("float_data-100-1.txt",'r')

#create an empty list:
data=[]		
while True:

	line = fp.readline()
	if line == "":
		break

	line = line.strip()
	word = line.split()
	item = float(word[0])
	data.append(item)

#sort list:
data.sort()

for i in xrange(len(data)):
	print data[i]

