class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next


class linkedListNode(Node):

    def __init__(self, key=None, next=None):
        super().__init__(key, next)
        self.head = None

    def append(self, node):
        if node is None:
            return
        node = linkedListNode(node)
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        return node


class completeBinaryTree(linkedListNode):

    def __init__(self, key=None, next=None):
        super().__init__(key, next)

    def findParent(node, index) -> Node:
        if index <= 0:
            raise ValueError("unvalid index")
        p = node
        count = 0
        while (count < index // 2):
            if p.next is None:
                raise ValueError("unvalid index")
            p = p.next
            count += 1
        return p

    def findLeftChild(node, index) -> Node:
        if index < 0:
            raise ValueError("unvalid index")
        p = node
        count = 0
        while (count != 2 * index + 1):
            if p.next is None:
                raise ValueError("unvalid index")
            p = p.next
            count += 1
        return p

    def findRightChild(node, index) -> Node:
        if index < 0:
            raise ValueError("unvalid index")
        p = node
        count = 0
        while (count != 2 * index + 2):
            if p.next is None:
                raise ValueError("unvalid index")
            p = p.next
            count += 1
        return p


class binaryHeap(completeBinaryTree):

    def __init__(self, key=None, next=None):
        super().__init__(key, next)

    def getIndex(self, node) -> int:
        if self.head is None:
            return
        elif self.head is node:
            return 0
        else:
            count = 1
            p = self.head
            while (p.next and p.next != node):
                p = p.next
                count += 1
            return count

    def swim(self, index: int):
        nodex = self.getNode(index)
        val = nodex.key
        parent = self.getNode(index // 2)
        if parent is not None:
            parentVal = parent.key
            while index > 0 and val < parentVal:
                temp = val
                nodex.key = parentVal
                parent.key = temp
                index = index // 2
                nodex = self.getNode(index)
                val = nodex.key
                parent = self.getNode(index // 2)
                if parent is not None:
                    parentVal = parent.key
                else:
                    break

    def getNode(self, index) -> Node:
        # if index == 0:
        #     return self.head
        # elif index == 1:
        #     return self.head.next
        # else:
        #     count = 0
        #     p = self.head
        #     while (count < index and p.next):
        #         count += 1
        #         p = p.next
        #     return p
        if index > 0:
            p = self.head
            count = 1
            while (count < index and p.next):
                p = p.next
                count += 1
            return p

    def sink(self, index):
        node = self.getNode(index)
        # while (2*index+ 1) <= self.size() - 1:
        #     if 2*index + 1 == self.size() - 1:
        #         if node.key > self.getNode(2*index + 1).key:
        #             p = self.head
        #             while (p.next):
        #                 p = p.next
        #             p.key , node.key = node.key ,p.key
        #         break
        #     elif node.key > min(self.getNode(2*index + 1).key,self.getNode(2*index + 2).key):
        #         if self.getNode(2*index + 1).key < self.getNode(2*index + 2).key:
        #             p = self.getNode(2*index + 1)
        #             p.key , node.key = node.key ,p.key
        #             index = 2*index + 1
        #         else:
        #             p = self.getNode(2*index + 2)
        #             p.key , node.key = node.key ,p.key
        #             index = 2*index + 2

        while (2 * index) <= self.size():
            if 2 * index == self.size():
                if node.key > self.getNode(2 * index).key:
                    p = self.head
                    while (p.next):
                        p = p.next
                    # p.key , node.key = node.key ,p.key
                    temp = p.key
                    p.key = node.key
                    node.key = temp

                break
            elif node.key > min(self.getNode(2 * index).key, self.getNode(2 * index + 1).key):
                if self.getNode(2 * index).key < self.getNode(2 * index + 1).key:
                    p = self.getNode(2 * index)
                    # p.key , node.key = node.key ,p.key
                    temp = p.key
                    p.key = node.key
                    node.key = temp

                    index = 2 * index
                else:
                    p = self.getNode(2 * index + 1)
                    # p.key , node.key = node.key ,p.key
                    temp = p.key
                    p.key = node.key
                    node.key = temp

                    index = 2 * index + 1
                node = self.getNode(index)
            else:
                break

    def insert(self, node):
        self.append(node)
        # index = self.getIndex(node)
        index = self.size()

        self.swim(index)

    def delMin(self):
        result = self.head.key
        prev = None
        p = self.head
        while (p.next):
            prev = p
            p = p.next
        self.head.key = p.key
        prev.next = None

        # print(self)

        # self.sink(0)
        self.sink(1)
        return result

    # def buildheap(self):
    #     i = self.size() // 2
    #     while i > 0:
    #         self.sink(i)
    #         i -= 1

    def size(self):
        if self.head is None:
            return 0
        count = 1
        p = self.head
        while (p.next):
            p = p.next
            count += 1
        return count

    # def __str__(self):
    #     """返回一个对象的描述信息"""
    #     value = []
    #     pointer = a.head
    #     while pointer is not None:
    #         value.append(pointer.key)
    #         pointer = pointer.next
    #     return value.__str__()


# if __name__ == "__main__":
#     a = binaryHeap()


#     a.insert(2)
#     a.insert(1)
#     a.insert(4)
#     a.insert(6)
#     a.insert(8)


#     print(a)

#     # print(a.delMin())
#     min = a.delMin()
#     print(min)

#     print(a)
def aperformance_test():
    a = binaryHeap()
    a.insert(2)
    a.insert(1)
    a.insert(4)
    a.insert(6)
    a.insert(8)
    a.delMin()
    a.delMin()