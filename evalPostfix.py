from Stack import Stack

operator = ["*","/","+","-"]

Expr = raw_input("Enter A Postfix Arithmetic Expression: ")

print Expr 

opStack=Stack()

for i in xrange(len(Expr)):

	if Expr[i]== " ":
		continue

	else:
		if not Expr[i] in operator:
			opStack.push(Expr[i])
	
		else:
			operand2= opStack.pop()		
			operand1= opStack.pop()
			operation = operand1 + Expr[i] + operand2
			print operation
			#the eval function returns a numeric value
			#Hence convert result to string before pushing
			#back onto the stack: 		
			result  = str(eval(operation))		
			print result
			opStack.push(result)


result = opStack.pop()


print "The Evaluation of PostFix Expression ",Expr, "is: ", result



	
