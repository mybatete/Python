fp=open("Salaries.dat",'r')

#create an empty dictionary:
salary={}		
while True:

	line = fp.readline()
	if line == "":
		break

	line = line.strip()
	word = line.split()
	key = word[0]
	item = float(word[1])
	salary[key]=item

for key in salary:
	print key,salary[key]

for (key,value) in salary.items():
	print key,value

Exists = salary.get("James","None")

print Exists

#sort keys:

myKeys = salary.keys()
myKeys.sort()

for key in myKeys:
        print key,salary[key]

