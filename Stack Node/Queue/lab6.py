from Queue2 import Queue2

fp = open ("test.txt","r")
#fp = open ("Linux_multipleQs-Jobs.dat", "r")
Q1 = Queue2()
Q2 = Queue2()
Q3 = Queue2()

while True:
    line = fp.readline()
    if line == "":
        break
    #split the text file into it's different parts
    line = line.strip()
    word = line.split()
    t = word[1].split("ms")
    task_time = float (t[0])
    Q1.enqueue(task_time)
COUNT1 = 0
TOTAL1 = 0
COUNT2 = 0
TOTAL2 = 0
COUNT3 = 0
TOTAL3 = 0
#check to see if the task's length qualifies for this run
while Q1.isEmpty() == False:
    a = Q1.dequeue().getData()
    if a > 3.0:
        b = a-3.0
        Q2.enqueue(b)
    if a<= 3.0:
        TOTAL1 += a
        COUNT1 +=1
print COUNT1, "Tasks executions Completed their Run on the first Queue"
print
print "the average execution time in Queue 1 is ", TOTAL1/COUNT1

#check to see if the task's length qualifies for this run
while Q2.isEmpty() == False:
    a = Q2.dequeue().getData()
    if a > 100.0:
        b = a - 100.0
        Q3.enqueue(b)
        
    if a <= 100.0:
        TOTAL2 += a
        COUNT2 += 1
print COUNT2, "Tasks executions Completed their Run on the second Queue"
print
print "the average execution time in Queue 2 is ", TOTAL2/COUNT2
#check to see if the task's length qualifies for this run
while Q3.isEmpty() == False:
    a = Q3.dequeue().getData()
    TOTAL3 += a
    COUNT3 +=1


print COUNT3, "Tasks executions Completed their Run on the Third Queue"
print
print "the average execution time in Queue 3 is ", TOTAL3/COUNT3
    
