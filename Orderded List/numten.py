from orderedListDL import orderedListDL

def main():
    x = input ("what is the range of the first list: ")
    y= input ("what is the range of the second list: ")
    l1 = orderedListDL()
    l2 = orderedListDL()
    for num in xrange(0,x,2):
        l1.add(num)
    for num in xrange(1,y,2):
        l2.add(num)

    result = mergeOrderedLinkedLists(l1,l2)
    print "mergeOrderedLinkedLists (l1 l2 ) = ", result.traversal()

def mergeOrderedLinkedLists(l1,l2):
    result = orderedListDL()
    

    while l1.isEmpty != True:
        c = l1.getHead()
        if c == None:
            break
        c =c.getData()
        
        l1.remove(c)
        result.add(c)

    while l2.isEmpty != True:
        c = l2.getHead()
        if c == None:
            break
        c = c.getData()
        
        l2.remove(c)
        result.add(c)

    return result
main()
