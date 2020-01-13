from mbinaryTree import BinaryTree
from binarySearchTree import BSTree
import random

def main():

    t = BSTree()
        
    for i in xrange(0,20):
        num = random.randint(0,100)
        print "num", num
        tree  = BinaryTree(num)
        root = t.getRoot()
        t.insertBST(root,tree)
       
        print t.getRoot().get_root_val()


main() 
