from Stack import Stack

#A python dictionary:
priority = {"*":2,"/":2,"+":1,"-":1,"(":0}

#A python List:
operator = ["*","/","+","-"]


Expr = raw_input("Enter An Infix Arithmetic Expression: ")

print Expr 

PostExpr=""

symStack=Stack()

for i in xrange(len(Expr)):

	if Expr[i] == " ":
		continue

	if Expr[i] == "(":
		symStack.push(Expr[i])

	elif Expr[i] == ")":

		symbol = symStack.pop()		
		while symbol != "(" :
			PostExpr += symbol		
			symbol = symStack.pop()		

	elif Expr[i] in operator:
		top = symStack.top()		
		while symStack.isEmpty()==False and \
			priority[Expr[i]] <= priority[top]:
			PostExpr += symStack.pop()	
			top = symStack.top()		
			
		symStack.push(Expr[i])
	else:
		PostExpr += Expr[i]

while not symStack.isEmpty():
	PostExpr += symStack.pop()		
		

print "Conversion of Infix Expression: ", Expr
print "To PostFix Expression         : ",PostExpr



	
