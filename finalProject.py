from findNodeMethod import *
import math
import time

#create a Complete Binary Tree from its linked list representation

# Linked List node
class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next
        

# Binary Tree Node structure
class BinaryTreeNode(Node):

    # Constructor to create a new node
    def __init__(self, key):
        super().__init__()
        self.key = key
        self.left = None
        self.right = None


    
 

# Class to convert the linked list to Binary Tree
class Conversion(BinaryTreeNode):

    # Constructor for storing head of linked list and root for the Binary Tree
    def __init__(self, data = None):

        self.head = None
        self.root = None
        self.rootHeap = None
        





    def append(self,node):
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


    def rootNode(self):
        q = []

        # Base Case
        if self.head is None:
            self.root = None
            return

        # 1. The first node is always the root node, and add it to the queue
        self.root = BinaryTreeNode(self.head.key)
        q.append(self.root)

        # Advance the pointer to the next node
        self.head = self.head.next

    # def convertList2Binary(self):

    #     # Queue to store the parent nodes
    #     q = []

    #     # Base Case
    #     if self.head is None:
    #         self.root = None
    #         return

    #     # 1. The first node is always the root node, and add it to the queue
    #     self.root = BinaryTreeNode(self.head.key)
    #     q.append(self.root)

    #     # Advance the pointer to the next node
    #     self.head = self.head.next

    #     # Until the end of linked list is reached, do:
    #     while(self.head):

    #         # 2.a) Take the parent node from the q and remove it from q
    #         parent = q.pop(0) # Front of queue

    #         # 2.c) Take next two nodes from the linked list.
    #         # I will add them as children of the current parent node in step 2.b.
    #         # append them into the queue so that they will be parent to the future node
    #         leftChild= None
    #         rightChild = None

    #         leftChild = BinaryTreeNode(self.head.key)
    #         q.append(leftChild)
    #         self.head = self.head.next
    #         if(self.head):
    #             rightChild = BinaryTreeNode(self.head.key)
    #             q.append(rightChild)
    #             self.head = self.head.next

    #         #2.b) Assign the left and right children of parent
    #         parent.left = leftChild
    #         parent.right = rightChild
    

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

            while (count != 2*index+1 and leftchild.next is not None):
                leftchild = leftchild.next
                count +=1 

            if (count == 2*index +1):
                p.left = leftchild

            if (leftchild.next is not None):                
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

            if (node.left is not None):
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
        p = self.head         
        while(p.next):
            p = p.next
        self.root = p
        p = None
        self.convert_CBT_2_MinimumPq()

    def insert(self,node):
        conv.append(node)
        conv.convert_Linkedlist_2_CBT()
        conv.convert_CBT_2_MinimumPq()
        

    def inorderTraversal(self, root):
        if(root):
            self.inorderTraversal(root.left)
            print (root.key,end=" ")
            self.inorderTraversal(root.right)

    def preorderTraversal(self, root):
        if(root):
            print (root.key,end=" ")
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)






# def convert_CBT_2_MinimumPq(node):

#     def dfs(node):

#         if not node:
#             return

#         dfs(node.right)
#         dfs(node.left)

#         if (node.left is not None):
#             if (node.key > node.left.key):
#                 p = node.key
#                 node.key = node.left.key
#                 node.left.key = p

#         if (node.right is not None):
#             if (node.key > node.right.key):
#                 p = node.key
#                 node.key = node.right.key
#                 node.right.key = p

#     dfs(node)


def performance_test():
    start = int(round(time.time() * 1000))
    start = int(round(time.time() * 1000))
    conv = Conversion()
    conv.append(100)
    conv.append(30)
    conv.append(25)
    conv.append(15)
    conv.append(12)
    conv.append(10)
    

    conv.convert_Linkedlist_2_CBT()
    conv.convert_CBT_2_MinimumPq()
    end = int(round(time.time() * 1000))
    print(f'{end - start}ms')






# # Driver code
if __name__ == "__main__":

    # conv = Conversion()
    # conv.append(36)
    # conv.append(30)
    # conv.append(25)
    # conv.append(15)
    # conv.append(12)
    # conv.append(10)

    # conv.convertList2Binary()
    # i = 3


    # # findParent(conv.root, node)
    # findParent(conv.root,i)


    conv = Conversion()
    conv.append(100)
    conv.append(30)
    conv.append(25)
    conv.append(15)
    conv.append(12)
    conv.append(10)
    

    conv.convert_Linkedlist_2_CBT()
    conv.convert_CBT_2_MinimumPq()
    
    # conv.convert_CBT_2_MinimumPq()
    conv.insert(3)
    conv.insert(34)

    # print ("Inorder Traversal of the constructed Binary Tree is:")
    # conv.inorderTraversal(conv.root)
    performance_test()
 