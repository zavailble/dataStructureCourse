# def flatten(root):
#     if (root == None or root.left == None and root.right == None):
#         return
#     if (root.left != None):
#         flatten(root.left) 
#         tmpRight = root.right
#         root.right = root.left
#         root.left = None
#         t = root.right
#         while (t.right != None):
#             t = t.right
#         t.right = tmpRight
#     flatten(root.right)


def findParent(node,index):
    if index <= 0 :
        raise ValueError("unvalid index")
    p = node
    count = 0

    while(count < (index - 1)//2):
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
    while(count != 2*index + 1):
        if p.next is None:
            raise ValueError("unvalid index")
        p = p.next
        count += 1
    print(p.key)


def findRightChild(node,index):
    if index < 0 :
        raise ValueError("unvalid index")
    p = node
    count = 0
    while(count != 2*index + 2):
        if p.next is None:
            raise ValueError("unvalid index")
        p = p.next
        count += 1
    print(p.key)


def findRightChild(node):
        if (node is None):
            raise ValueError("node is not in the tree")
        elif (node.right is None):
            raise ValueError("node doesn't have right child")
        else:
            print(node.right.key)
