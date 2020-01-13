from Stack import Stack

tackyStack= Stack()

FileName=raw_input("Enter File Name: ")
OutFile= FileName.split(".")
NewFile= str(OutFile[0]) + "-Rev.txt"

fp = open(FileName, "r")
fpOut = open(NewFile, "w")

print "reading File ...."
while True :

	text = fp.readline()
	
	if text == "":
		break

	tackyStack.push(text)


while not tackyStack.isEmpty():
	revText = tackyStack.pop()
	fpOut.write(revText)


fp.close()
fpOut.close()


