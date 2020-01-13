from Stack import Stack

word = raw_input("Enter a word: ")
word = word.upper()

wordStack= Stack()

for letter in word:

	wordStack.push(letter) 

print "\n\n"

reverse=""
while not wordStack.isEmpty():
	reverse += str(wordStack.pop())

print reverse

if word == reverse:
	print word, "is a palindrome ... :-)"
else:
	print word, "is a NOT a palindrome ... :-)"

print "\n\n"


