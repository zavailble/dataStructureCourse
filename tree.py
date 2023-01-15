from findNodeMethod import *
import math

class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next
        


class BinaryTreeNode(Node):

    def __init__(self, key):
        super().__init__()
        self.key = key
        self.left = None
        self.right = None


    
class binaryHeap(BinaryTreeNode):

    def __init__(self, data = None):        
        self.head = None
        self.root = None
        self.rootHeap = None
        
    def  append(self,node):
        if node is None:
            return 
        node = BinaryTreeNode(node)
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        return node
    

    def convert_Linkedlist_2_CBT(self):
        if self.head is None:
            self.root = None
            return
        self.root = self.head    
        p = self.head
        index = 0
        while(p):
            count = 0
            leftchild = self.head

            while (count != 2*index+1 and leftchild.next is not None and leftchild.next.key is not None):
                leftchild = leftchild.next
                count +=1 

            if (count == 2*index +1):
                p.left = leftchild

            if (leftchild.next is not None and leftchild.next.key is not None):                
                p.right = leftchild.next    

            index += 1
            p = p.next    


    def tree_height(self):
        p = self.root
        if (p is None):
            return 0
        elif (p.next is None):
            return 1
        
        else: 
            count = 1   
            while(p.next):
                count +=1
                p = p.next
            height = math.floor(math.log2(count))
            return height    


    def convert_CBT_2_MinimumPq(self):
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            dfs(node.left)

            if (node.left is not None and node.left.key is not None):
                if (node.key > node.left.key):
                    p = node.key
                    node.key = node.left.key
                    node.left.key = p
                    dfs(node.left)
            if (node.right is not None):
                if (node.key > node.right.key):
                    p = node.key
                    node.key = node.right.key
                    node.right.key = p        
        for i in range(self.tree_height()):            
            dfs(self.root)


    def delMin(self):
        self.root.key = self.root.next.key        
        self.root.next = self.root.next.next
        self.convert_Linkedlist_2_CBT()
        self.convert_CBT_2_MinimumPq()


    def insert(self,node):
        self.append(node)
        self.convert_Linkedlist_2_CBT()
        self.convert_CBT_2_MinimumPq()
        

    # def inorderTraversal(self, root):
    #     if(root):
    #         self.inorderTraversal(root.left)
    #         print (root.key,end=" ")
    #         self.inorderTraversal(root.right)


    # def preorderTraversal(self, root):
    #     if(root):
    #         print (root.key,end=" ")
    #         self.preorderTraversal(root.left)
    #         self.preorderTraversal(root.right)




def perfomance_test():
    conv = binaryHeap()
    conv. insert(2)
    conv. insert(1)
    conv. insert(4)
    conv. insert(6)
    conv. insert(8)
    conv.delMin()
    conv.delMin()

    # print ("Inorder Traversal of the constructed Binary Tree is:")
    # conv.Traversal(conv.root)

 
    # my_test(benchmark=performance_test)
