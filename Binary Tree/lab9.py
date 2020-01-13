from mbinaryTree import BinaryTree

l=[]
t=BinaryTree()
    
    
for i in range(0,10):
        l.append(i)
for item in l:
    if (item < 5):
            t.inser_left(item)
    else:
        t.insert_right(item)
            
        
def insertBST(root, nn):

        
    if root=="NULL":
        root=BinaryTree(nn)
        set_root_val(root)

    else:
        current=get_root_val(root)
        while(current.isEmpty==False):
            parent=current
            if(nn<current):
                current=current.get_left_child()
                print new.current
            else:
                current=current.get_right_child()

            
                
            
        
    
