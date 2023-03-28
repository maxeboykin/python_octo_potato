print('-------------------------------------------------------')
print('linked list cycles')


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(node):
    slow, fast = node, node
    first_iteration = True
    while fast is not None and fast.next is not None:
        if slow == fast and not first_iteration:
            return True
        first_iteration = False
        slow = slow.next
        fast = fast.next.next
    return False


def get_cycle_length(node):
    slow, fast = node, node
    first_iteration = True
    while fast is not None and fast.next is not None:
        if slow == fast and not first_iteration:
            return find_cycle_length(slow)
        first_iteration = False
        slow = slow.next
        fast = fast.next.next


def find_cycle_length(slow):
    looping_node = slow
    first_iteration = True
    count = 0
    while slow != looping_node or first_iteration:
        count += 1
        first_iteration = False
        looping_node = looping_node.next
    return count


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
print("LinkedList has cycle: " + str(has_cycle(head)))

head.next.next.next.next.next.next = head.next.next
print("LinkedList has cycle: " + str(has_cycle(head)))
print("LinkedList cycle length: " + str(get_cycle_length(head)))
head.next.next.next.next.next.next = head.next.next.next
print("LinkedList has cycle: " + str(has_cycle(head)))
print("LinkedList cycle length: " + str(get_cycle_length(head)))