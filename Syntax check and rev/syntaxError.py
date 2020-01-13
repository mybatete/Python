import sys
from Stack import Stack

def main():

	OPEN  = "{"
	CLOSE = "}"

	s = Stack()	

	fileName = raw_input("Enter File Name: ")

	try:
		fp = open(fileName, "r")
	except IOError:
		sys.exit("\n\n\nUnable to Open File!!!\n\n\n")

	lineNo = 0
	while True:
		line = fp.readline()
		lineNo += 1

		if line == "":
			break
		
		for i in xrange(0,len(line)):

			print line[i]		
			if line[i] == OPEN:
				s.push(OPEN)
			
			else:

				if line[i] == CLOSE:
					if s.isEmpty():
						print "\n\nSyntax Error on Line: %d\n%s\n\n" % (lineNo,line)
						exit()
					else:
						s.pop()	


	if not s.isEmpty():
		print "\n\nSyntax Error on Line: %d\n%s\n\n" % (lineNo,line)
		exit()
main()



