print('-------------------------------------------------------')
print('middle of a linked list')

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_middle_of_linked_list(node):
    slow, fast = node, node
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("LinkedList has cycle: " + str(find_middle_of_linked_list(head)))

print("Middle Node: " + str(find_middle_of_linked_list(head).value))

head.next.next.next.next.next = Node(6)
print("Middle Node: " + str(find_middle_of_linked_list(head).value))

head.next.next.next.next.next.next = Node(7)
print("Middle Node: " + str(find_middle_of_linked_list(head).value))