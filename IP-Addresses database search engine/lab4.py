"""
Program: IP-Addresses database search engine
Name: Batete Yedidia Marc
Date: 09/27/2018
Despription: the program creates a database  using an ordered singly linked list
 for an easier manipulation of student internet history.
Input:
    file: Residence_Hall_IPs.dat
    search address from the user
Output:
    -IP addresse
    - frequency conexion
"""

from ListNode import Node

def main():
    IPList = orderedList()

    # the program reads from the file
    fp1 = open("output.txt", 'w')
    
    List = readFile("Residence_Hall_IPs.dat")

    #add the adresses to the ordered list
    for address in List:
        update = IPList.update(address)
        if update == False:
            newaddr = IPaddress(address)
            IPList.add(newaddr)

    #traverses the list and return the frequency of connection 
    IPList.traversal(fp1)

    
    repeat = True
    while repeat != False:
        rp = raw_input("Would you like to search more items? y/n: ")
        if rp.lower() == "n":
            repeat = False
        else:
            search = raw_input("Enter the IP Address you want to find: ")
            IPList.search(search, fp1)

            

def readFile(fileName):
    fp = open(fileName, 'r')
    List =[]

    while True:
        line = fp.readline()
        if line == "":
            break
        line = line.strip()
        item = line.split()
        List.append(item[0])     
    return List

class IPaddress:
    
    def __init__(self, IPAddress):
        self.IPAddress = IPAddress
        self.count = 1
    
    def getIP(self):
        return self.IPAddress

    def getCount(self):
        return self.count

    def setIP(self, address):
        self.address = address

    def setCount(self):
        self.count += 1

class orderedList:

    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head

    def isEmpty(self):
        return self.head == None

    def add(self, item):
       
        if self.head == None:
            temp      = Node(item)
            temp.setNext(self.head)
            self.head = temp
        else:
            current  = self.head
            previous = None

            while current != None:
                if current.getData().getIP() > item.getIP():
                    break

                previous = current
                current  = current.getNext()
            
            temp        = Node(item)
            
           
            if previous == None:
                temp.setNext(self.head)
                self.head = temp
            
            
            else:
               
                temp.setNext(current)
                previous.setNext(temp)


    def size(self):
        current = self.head
        count    = 0
    
        while current != None:

            count += 1
            current = current.getNext()

        return count


    def remove(self,item,file):
        current  = self.head
        previous = None
        count    = 0
        found    = False

        print "Searching List for item", item
        while current != None:

            if current.getData().getIP() == item:
                file.write("Item Found: %s at location: %i" % current.getData().getIP(), count)
                found = True
                break
            
            if current.getData().getIP() > item:
                found = False
                break

            previous = current
            current  = current.getNext()
            count   += 1
        
        if found:
            
            file.write("Removing item: %s" % item)
            if previous != None:
                new_next  = current.getNext()
                previous.setNext(new_next)
            else:
                self.head = current.getNext() 

        else:
            file.write("Item: %s Was Not Found On List" % item)

        return found

    def index(self,item, file):
        current  = self.head
        position = 0
        found    = False

        file("Searching List for item...%s" % item)
        while current != None:

            if current.getData().getIP() == item:
                print file.write("Item Found: %s at location: %i" % current.getData().getIP(), position)
                found = True
                break

            if current.getData().getIP() > item:
                found = False
                break

            current   = current.getNext()
            position += 1

        if not found:
            file.write("Item: %s Was Not Found On List" % item)
            position = -1

        return position

    def update(self,item):
        current = self.head
        count   = 0
        found   = False
        while current != None:

            if current.getData().getIP() == item:
                found = True
                current.getData().setCount()
                break

            if current.getData().getIP() > item:
                found = False
                break

            current = current.getNext()
            count  += 1
        return found

    def traversal(self, file):
        current = self.head
        count    = 1

        file.write("\nIP Address          Number of access")
        file.write("\n===============     ================")
                
        while current != None:           
            file.write('\n%-15s %20i' %(current.getData().getIP() ,current.getData().getCount())) 
            current = current.getNext()
            count += 1

    def search(self, item,File):
        current = self.head
        count = 1
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData().getIP() == item:
                found = True
                File.write("\n\nFound IP address: %s" % current.getData().getIP())
                File.write("\nThe position in the database: %i " % count)
                File.write("\nThe access count: %s " % current.getData().getCount())
            else:
                if current.getData().getIP() > item:
                    stop = True
                else:
                    current = current.getNext()
            count += 1
        if not found:
            File.write("The item was not found.")
        
        return found

main()
