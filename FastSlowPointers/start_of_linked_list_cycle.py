print('-------------------------------------------------------')
print('start of the linked list cycle')


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_cycle_start(node):
    slow, fast = node, node
    left, right = node, node
    first_iteration = True
    cycle_length = 0
    while fast is not None and fast.next is not None:
        if slow == fast and not first_iteration:
            cycle_length = get_cycle_length(slow)
            break
        first_iteration = False
        slow = slow.next
        fast = fast.next.next
    for i in range(0, cycle_length, 1):
        right = right.next
    while left != right:
        left = left.next
        right = right.next

    return left


def get_cycle_length(slow):
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

head.next.next.next.next.next.next = head.next.next
print("LinkedList cycle start: " + str(find_cycle_start(head).value))

head.next.next.next.next.next.next = head.next.next.next
print("LinkedList cycle start: " + str(find_cycle_start(head).value))

head.next.next.next.next.next.next = head
print("LinkedList cycle start: " + str(find_cycle_start(head).value))
