
LOWCUTOFF=50
HIGHCUTOFF=100

reading1=input("Enter first pollution reading: ")
reading2=input("Enter second pollution reading: ")
reading3=input("Enter second pollution reading: ")

averageReading = (reading1 + reading2 + reading3)/3.0

if averageReading < LOWCUTOFF :
	print "\nGood Condition!!!\n"

elif (averageReading >= LOWCUTOFF) and (averageReading < HIGHCUTOFF) :
	print "\nFair Condition!!!\n"
else:
	print "\n\tPoor Condition!!!\n"
	print "\nLewis-Clark Valley ... Oh No!\n\n"


