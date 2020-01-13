from Stack import Stack

value = input("Enter a Positive Integer: ")

binStack= Stack()

while value > 0 :

	remainder = value % 2
	binStack.push(remainder) 
	value    /= 2

print "\n\n"

binary=""
while not binStack.isEmpty():
	binary += str(binStack.pop())

print binary

