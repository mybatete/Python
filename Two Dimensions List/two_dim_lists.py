def main():
	'''
	This program reads employee record information and generates
	employee report sumaries
	'''

	employee=[]

	employee = read_file()

	#av_age = average(employee,i)

	#print av_age	

	print len(employee)

	for row in xrange(len(employee)):
		for col in xrange(len(employee[0])):
			print employee[row][col] 
'''
	for row in employee:
		for col in row:
			print col 

	for i in employee:
		print i[0] 

	for worker in employee:
		print worker[0] 
'''
	#for i in age:
		#print i

def read_file():
	filename=raw_input("Enter File Name: ")

	fp=open(filename,'r')

	line = fp.readline()

	list = []
	while True:
		line = fp.readline()
		
		if line == "":
			break

		line = line.strip()
		word = line.split()
		list.append(word)

	fp.close()
	
	return list
'''
def average(list):

	sum = 0

	for i in list:
		sum += i

	average = sum/float(len(list))
	return average
'''
main()


