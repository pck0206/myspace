# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# def traverseAndPrint(head):
#     currentNode = head
#     while currentNode:
#         print(currentNode.data, end=" -> ")
#         currentNode = currentNode.next
#     print("null")
#
# node1 = Node(7)
# node2 = Node(11)
# node3 = Node(3)
# node4 = Node(2)
# node5 = Node(9)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.head = node5
#
# traverseAndPrint(node1)



# class Node:
#     def __init__(self,data,next = None):
#         self.next = next
#         self.data = data
# def min_value(head):
#     ming = head.data
#     cur = head
#     while cur:
#         print(cur.data,end = " -> ")
#         if cur.data < ming:
#             ming = cur.data
#         cur = cur.next
#     print("Null")
#     print(ming)
# node1 = Node(2)
# node2 = Node(3)
# node3 = Node(-1)
#
# node1.next = node2
# node2.next = node3
#
# min_value(node1)



# class linkedlistNode:
#     def __init__(self,value,next = None):
#         self.value = value
#         self.next = next 
# class Node:
#     def __init__(self,head = None):
#         self.head = head
#     def insert(self,value):
#         node = linkedlistNode(value)
#         if self.head is None:
#             self.head = node
#             return
        
#         cur = self.head
#         while True:
#             if cur.next == None:
#                 cur.next = node
#                 break
#             cur = cur.next
#     def print(self):
#         cur = self.head
#         while cur is not None:
#             print(cur.value,end = "-->")
#             cur = cur.next
#         print("Null")
# a = Node()
# a.print()
# a.insert("3")
# a.print()
# a.insert("10")
# a.print()
# a.insert("100")
# a.print()
