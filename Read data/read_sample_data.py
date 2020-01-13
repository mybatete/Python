#Read File: sample_data.txt
#inputdata=raw_input("Enter File Name: ")
#fp = open(inputdata,'r')

fp = open("sample_data.txt",'r')

while True:

	#Read the next line in the file:
	line = fp.readline()

	#check if line is empty:
	#That is if end of the file:
	if line == "":
		break	

	#Remove all blanks at the beginning and end of line:
	line = line.strip()
	
	#Break up the line into array of values (columns)
	word = line.split()


	#Convert the text in column zero into integers:
	index  = int(word[0])

	#Convert the text in column one into integers:
	length = int(word[1])
	
	#Convert the text in column two into real numbers:
	data   = float(word[2])

	print "Line Reading is %d\t%d\t%f\n" % (index, length, data)

