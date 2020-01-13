STEP=1

def main():

	disks =int(input("Enter the Number of Disks: "))

	print "\n\n\n"

	if disks < 1:
		print "\n\nNumber of Disks Selected is Less Than 1!!!\n\n"
	else:
		#Move Disks from Source A to Destination C, Use B as the Auxiliary 
		towers(disks, "A", "C", "B")

	print "\n\n\n"

	return


def towers(disks, source, dest, aux):

	global STEP
	print "Towers(",disks,",", source,",", dest, ",",aux,")"

	#Base Case: Move 1 Disk From Source to Destination Disk
	if disks == 1:
		print "\t\t\tStep ", STEP, ": Move Disk From", source, "to", dest 
		STEP += 1
	else:

		#General Case: Move n-1 Disk From Source to Auxiliary Disk
		#	     : Use Destination Disk as Intermediary
		towers(disks-1, source, aux, dest)

		print "\t\t\tStep ", STEP, ": Move Disk From", source, "to", dest 
		STEP += 1

		#General Case: Move n-1 Disk From Auxiliary to Destination Disk
		#	     : Use Source Disk as Intermediary
		towers(disks-1, aux, dest,source)
		
	return

main() 
