from Queue2 import Queue2

#Create an empty Python dictionary:
instr={}

#Create a Queue Object:
CPUsim=Queue2()

fp  = open("instruction_times.dat","r")
fp1 = open("instruction_simFile.dat","r")

while True:
	line = fp.readline()
	
	if line=="":
		break

	line = line.strip()
	word = line.split()

	#Insert the name of instruction and execution time:	
	instr[word[0]]=int(word[1])


print "A total of ", len(instr), "Instruction Types in File"

while True:
	line = fp1.readline()
	
	if line=="":
		break

	line = line.strip()
	word = line.split()
	
	CPUsim.enqueue(word[0])


CPUsim.traversal()

print "Program Contains: ", CPUsim.size(), "Instructions."

total_time=0
cnt = CPUsim.size()
while not CPUsim.isEmpty():
	current = CPUsim.dequeue()
	code    = current.getData() 

	total_time += instr[code]
	print total_time

print "\n\n\n"
print "Program Contains           : ",cnt, "Instructions."
print "Total Execution Time is    : ",total_time, "nanoseconds." 
print "Average Instruction Time is: ",float(total_time)/cnt, "nanoseconds." 
print "\n\n\n"

fp.close()
fp1.close()

