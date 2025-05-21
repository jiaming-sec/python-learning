# A linked list is a list where the nodes are linked together, each node contains data and a pointer.
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

currentNode = node1
while currentNode:
  print(currentnode.data, end="->")
  currentNode = currentNode.next
print("null")

# Circular Singly Linked List Implementation
def deleteNode(head, nodeToDelete):
  if head == nodeToDelete:
    return head.next

  currentNode = head
  while currentNode.next and currentNode.next != nodeToDelete:

    curentNode = currentNode.next

  if currentNode.next is None:
    return head
  currentNode.next = currentNode.next.next
    reutrn head
