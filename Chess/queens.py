import numpy
from Stack import Stack
from chessNode import Pos

def main():

	NUM=input("Enter Max Board Size : ")

	if NUM < 5:
		print "\n\nNo Solution Exists For Values Less Than 4\n"
		print "Choose A Value Greater Than 4\n\n"
		exit()


	board = createBoard(NUM)

	displayBoard(board,NUM)
	queens = Stack()
	assignQueens(queens,board,NUM)
	displayBoard(board,NUM)


def assignQueens(queens,board,NUM):
	bsize = NUM-1

	row = 1
	col = 0

	while (row <= bsize):
	
		while col <= bsize and row <= bsize:

			col += 1

			if not guarded(board,row,col,bsize):
				board[row][col] = 1
				posn = Pos(row,col)
				queens.push(posn)
				row += 1
				col  = 0
			else:
				while col >= bsize:
					posn = queens.pop()
					row  = posn.getRow()
					col  = posn.getCol()
					board[row][col] = 0
		


def guarded(board,newRow,newCol,NUM):
	bsize = NUM-1

	#checking if column is unsafe
	print "checking if column is unsafe..."
	col   = newCol
	row   = 1
	while row <= newRow:
		if board[row][col] == 1:
			print row, col, board[row][col]
			return True

		row += 1
	
	#checking if diagonal up and right is unsafe
	print "checking if diagonal up and right is unsafe..."
	col   = newCol+1
	row   = newRow-1
	while row > 0 and col <= bsize:
		if board[row][col] == 1:
			return True

		row -= 1
		col += 1
	
	#checking if diagonal up and left is unsafe
	print "checking if diagonal up and left is unsafe ..."
	col   = newCol-1
	row   = newRow-1
	while row > 0 and col > 0:
		if board[row][col] == 1:
			return True

		row -= 1
		col -= 1
	
	return False	




def createBoard(NUM):

	size = [0] * NUM
	temp = [size] * NUM

	board = numpy.array(temp)

	return board

def displayBoard(board,NUM):
	print "\n\n\n\n"
	print board
	print "\n\n\n\n"

	for i in xrange(1,NUM):
		for j in xrange(1,NUM):
			if board[i][j]==1:
				print "%2s" % "Q",
			else:
				print "%2d" % board[i][j],

		print "\n"
main()

