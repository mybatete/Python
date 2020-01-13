from orderedListDL import orderedListDL

L1 = orderedListDL()
L2= orderedListDL()
for num in xrange(0,20,2):
    L1.add(num)
for num in xrange(1,20,2):
    L2.add(num)


L1.traversal()
L2.traversal()

L3 = orderedListDL()

c=L1.remove(2)
print c
