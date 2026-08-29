"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        list_copy = list_to_arr(head)

        
        return arr_to_list(list_copy)


def loop_through_linked_list(head: Node):

    curr = head
    while curr is not None:
        yield curr
        curr = curr.next


def list_to_arr(linked_list: Node) -> list:
    new_list =[]

    if linked_list is None:
        return []
    
    for node in loop_through_linked_list(linked_list):
        new_list.append(node)
    return new_list

def arr_to_list(arr: list):
    if not arr:
        return None

    nodes = [
        Node(node.val) # val is the only field we can use to avoid using the original pointers from the list
        for node in arr
    ]

    copy_of = dict(zip(arr, nodes))

    for index, node in enumerate(nodes):
        original = arr[index]

        if index < len(nodes) - 1:
            node.next = nodes[index + 1]

        node.random = copy_of.get(original.random)

    return nodes[0]


