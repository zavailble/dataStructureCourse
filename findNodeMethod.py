import math
def flatten(root):
  
    # Base condition- return if root is None or if it is a leaf node
    if (root == None or root.left == None and root.right == None):
        return
      
    # If root.left exists then we have 
    # to make it root.right
    if (root.left != None):
  
        # Move left recursively
        flatten(root.left)
     
        # Store the node root.right
        tmpRight = root.right
        root.right = root.left
        root.left = None
  
        # Find the position to insert the stored value   
        t = root.right
        while (t.right != None):
            t = t.right
  
        # Insert the stored value
        t.right = tmpRight
  
    # Call the same function for root.right
    flatten(root.right)

def findParent(node,index):

    # flatten(node)

    if index <= 0 :
        raise ValueError("unvalid index")

    p = node
    count = 0

    while(count < math.floor((index - 1) / 2)):
        if p.next is None:
            raise ValueError("unvalid index")
        p = p.next
        count += 1
    print(p.key)


def findLeftChild(node,index):
    
    flatten(node)
    
    if index < 0 :
        raise ValueError("unvalid index")

    p = node
    count = 0

    while(count != 2*index+1):
        if p.next is None:
            raise ValueError("unvalid index")
        p = p.next
        count += 1
    print(p.key)


def findRightChild(node,index):

    flatten(node)

    if index < 0 :
        raise ValueError("unvalid index")

    p = node
    count = 0

    while(count != 2*index+2):
        if p.next is None:
            raise ValueError("unvalid index")
        p = p.next
        count += 1
    print(p.key)





#Find the parent of the given node
# def findParent(node, val, parent = -1):
#     if (node is None):
#         return

#     # If current node is the required node
#     if (node.key == val):

#         # Print its parent
#         print(parent)
#     else:

#         # Recursive calls for the children of the current node
#         # Current node is now the new parent
#         findParent(node.left, val, node.key)
#         findParent(node.right, val, node.key)

# #Find the left child of the given node
# def findLeftChild(node, val):
#     if (node.left is None):
#         raise ValueError("node is not in the tree") 

#     # If current node is the required node
#     if (node.key == val):

#         # Print its parent
#         print(node.left.key)
#     else:

#         # Recursive calls for the children of the current node
#         # Current node is now the new parent
#         findParent(node.left, val)
#         findParent(node.right, val)

# #Find the right child of the given node
# def findRightChild(node):
#         if (node is None):
#             raise ValueError("node is not in the tree")
#         elif (node.right is None):
#             raise ValueError("node doesn't have right child")
#         else:
#             print(node.right.key)





    # def push(self, new_data):

    #     # Creating a new linked list node and storing data
    #     new_node = Node(new_data)

    #     # Make next of new node as head
    #     new_node.next = self.head

    #     # Move the head to point to new node
    #     self.head = new_node