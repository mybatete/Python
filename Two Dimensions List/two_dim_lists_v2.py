'''
This program reads employee record information and generates
employee report sumaries
'''

fp=open("Boeing_Employees.dat",'r')

employee=[]

line = fp.readline()

while True:
	line = fp.readline()
	
	if line == "":
		break

	line = line.strip()
	word = line.split()
	employee.append(word)


print "The Number of Boeing Employees is: ", len(employee)



'''
for row in xrange(len(employee)):
	for col in xrange(len(employee[0])):
		print employee[row][col],
	print 
'''

'''
for row in xrange(len(employee)):
	print employee[row]

'''

'''
for row in xrange(len(employee)):
	for col in xrange(len(employee[0])):
		print employee[row][col],
	print 
'''

'''
for row in xrange(len(employee)):
	for col in xrange(len(employee[0])):
		print employee[row][col] 
'''

'''
for row in employee:
	for col in row:
		print col 
'''

'''

#Print Specific Columns in Table:
for worker in employee:
	print worker[0] 
'''

	


