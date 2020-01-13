from mbinaryTree import BinaryTree


class BSTree:
    def __init__ (self):
        self.root = None

    def getRoot(self):
        return self.root

    def isEmpty(self):
        return self.root == None

    def insertBST(self,root, newNode):
        if root == None:
            self.root = newNode
        else:
            current = self.root
            while current != None:
                parent = current
                if newNode.get_root_val() < current.get_root_val():
                    current = current.get_left_child()
                else:
                    current = current.get_right_child()

            if newNode.get_root_val() < parent.get_root_val():
                self.root.insert_left(newNode)
            else:
                self.root.insert_right(newNode)

