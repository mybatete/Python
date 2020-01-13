import sys
from shutil import copyfile

def main():

	fileName = raw_input("Enter Input File Name: ")
	Num      = int(input("Number of Records to Read Per Sort: "))
	
	mergeSort(fileName,Num)

	return
	

def mergeSort(fileName,Num):
	mList = []
	cnt   = 0

	file1="first-" +fileName
	file2="second-"+fileName
	file3="msorted-"+fileName
	
	try:
		fp = open(fileName, "r")
	except IOError:
		sys.exit("\n\n\nUnable to Open File!!!\n\n\n")

	while cnt == 0 or Num < cnt: 

		fp  = open(fileName, "r")
		fp1 = open(file1, "w")
		fp2 = open(file2, "w")
		fp3 = open(file3, "w")

		cnt = sortSubLists(fp,fp1,fp2,Num)

		print "\n\nNumber of Entries in Data File is: %d\n\n" % (cnt)

		mergeFiles(file1,file2,file3,Num)
		copyfile(file3,fileName)

		Num *= 2

def mergeFiles(file1,file2,file3,Num):
	fp1 = open(file1, "r")
	fp2 = open(file2, "r")
	fp3 = open(file3, "w")

	mList1 = []
	mList2 = []

	while True:


		mList1=getNextNum(fp1,mList1,Num)
		mList2=getNextNum(fp2,mList2,Num)
			
		cnt1 = len(mList1)
		cnt2 = len(mList2)

		mergeSubLists(mList1,mList2,fp3)

		if cnt1 == 0 or cnt2 == 0:
			break

	fp3.close()

	return

def getNextNum(fp,mList,Num):

	mList = []
	for i in xrange(Num):
		line = fp.readline()

		if line == "":
			break
		
		line  = line.strip()
		word  = line.split()
		value = float(word[0])

		mList.append(value)

	return mList				

def mergeSubLists(mList1,mList2,fp3):
	i = 0
	j = 0

	num1= len(mList1)	
	num2= len(mList2)	

	if num2==0 and num1>0:
		for i in mList1:
			fp3.write("%f\n" % (i))
		
	elif num1==0 and num2>0:
		for i in mList2:
			fp3.write("%f\n" % (i))
		
	else:
		while i<num1 or j < num2:

			if mList1[i] < mList2[j]:
				fp3.write("%f\n" % (mList1[i]))
				i += 1
	
				if i==num1:
					mList1.append(99999999999.99)
			else:
				fp3.write("%f\n" % (mList2[j]))
				j += 1
	
				if j==num2:
					mList2.append(99999999999.99)

	return


def sortSubLists(fp,fp1,fp2,Num):
	cnt   = 0
	batch = 0
	while True:

		mList    = []
		
		for i in xrange(Num):
			line = fp.readline()

			if line == "":
				break
		
			line  = line.strip()
			word  = line.split()
			value = float(word[0])

			mList.append(value)
					
			cnt  += 1 

		mList = insertionSort(mList)

		if batch % 2 == 0:
			append2File(fp1,mList)
		else:
			append2File(fp2,mList)

		batch += 1

		if line == "":
			break
		
	fp.close()
	fp1.close()
	fp2.close()

	return cnt

def append2File(fp,mList):

	for i in mList:
		fp.write("%f\n"%(i)) 


def insertionSort(myList):

	print "\n"
	current = 1
	last = len(myList) - 1

	while current <= last :

		value = myList[current]

		index =  current - 1

		#print "Pass:", current, "\n"

		while ( index >=0 and value < myList[index]):
			#print "Index: %d ... Comparing %d\t%d\n" % (index, value, myList[index])
		
			myList[index + 1] = myList[index]
			index             = index -1

		myList[index + 1] = value

		#print myList, "\n"

		current = current + 1

	return myList

main()
