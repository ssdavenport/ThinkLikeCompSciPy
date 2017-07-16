class Node(object):
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3




def printList(node):
    output = ["["]
    while node:
        output.append(str(node))
        node = node.next
        output.append(",")
    del(output[-1])
    output.append("]")
    print("".join(output))

def printBackward(list):
    if list == None: return
    head = list
    tail = list.next
    printBackward(tail)
    print(head,)


def removeSecond(list):
    first = list
    second = first.next
    third = second.next
    first.next = third
    second.next = None
    return(second)

def printBackwardNicely(list):
    print("[")
    printBackward(list)
    print("]")

printList(node1)
printBackwardNicely(node1)

print(removeSecond(node1))
printList(node1)