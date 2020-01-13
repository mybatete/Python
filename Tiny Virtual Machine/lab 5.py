"""
Program: Tiny	Virtual	Machine
author: Batete Yedidia Marc
date:09/27/2018
description: the progrgam reads from a file containing commands and follows along to create a stacked list
input:
    -file: sample_bytecode.asm
    
output:
    stacked list
"""
from Stack import Stack
#the program opens the file with the handle fp
fp =  open( "sample_bytecode.asm", "r")
# create a stack object
temp = Stack()
#loop through the file to read the commands
while True:
    line = fp.readline()
    if line == "":
        break
    line = line.strip()
    word = line.split()
    Instruction_name = word[0]
    #add a value
    if Instruction_name == "PUSHX":
        parameter = word [1]
        temp.push(parameter)
    #duplicate a value
    elif Instruction_name == "DUP":
        i = temp.pop()
        temp.push(i)
        temp.push(i)
    #ADD a divided value
    elif Instruction_name == "DIV":
        a= int(temp.pop())
        b= int(temp.pop())
        c= a/b
        temp.push(c)
    #add an increased by one value
    elif Instruction_name == "INCL":
        a = int(temp.pop())
        b = a+1
        temp.push(b)
    #add a multiplied value
    elif Instruction_name == "MULT":
        a = int(temp.pop())
        b = int(temp.pop())
        c = a * b
        temp.push(c)
    #add a decreased value
    elif Instruction_name == "DECL":
        a = int(temp.pop())
        b = a-1
        temp.push(b)
    #swap two values in the stack
    
    elif Instruction_name == "SWAP":
        a = int(temp.pop())
        b = int(temp.pop())
        temp.push(a)
        temp.push(b)
    elif Instruction_name == "PRINT":
        temp.top()
    elif Instruction_name == "EXIT":
        while temp.isEmpty() == False:
            temp.pop()
    #shift a value to the left.
    elif Instruction_name == "SHR":
        parameter = int(word [1])
        a = int(temp.pop())
        b = a>>parameter
        temp.push(b)
    #shift a value to the left.
    elif Instruction_name == "SHL":
        parameter = int(word [1])
        a = int(temp.pop())
        b = a<<parameter
        temp.push(b)
    elif Instruction_name == "AND":
        a = int(temp.pop())
        b = int(temp.pop())
        c = a&b
        temp.push(c)
    elif Instruction_name == "POPX":
        parameter= word[1]
        print parameter
        parameter = (temp.pop())
        print parameter
        
    elif Instruction_name == "OR":
        a = int(temp.pop())
        b = int(temp.pop())
        c = a/b
        temp.push(c)
        
    elif Instruction_name == "XOR":
        a = int(temp.pop())
        b = int(temp.pop())
        c = a^b
        temp.push(c)
    #add an the sum of two values.
    elif Instruction_name == "ADD":
        a = int(temp.pop())
        b = int(temp.pop())
        c = a + b
        temp.push(c)
    #add a substracted value
    elif Instruction_name == "SUB":
        a = int(temp.pop())
        b = int(temp.pop())
        c = a - b
        temp.push(c)
temp.traversal()
        
        
        
