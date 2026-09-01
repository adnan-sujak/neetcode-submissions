# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from itertools import batched, chain

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        
        groups = batched(iter_nodes(head), k)

        reverse_groups = ( # iterable comprehnsion
            reverse_group(list(group), k)
            for group in groups
        )
        
        #print(groups)
        #print(reverse_groups)
        merged = list(chain.from_iterable(reverse_groups))
        #relink after this
        #print(merged)

        return re_linked(merged)


def iter_nodes(head: ListNode):
    curr = head
    while curr:
        yield curr
        curr = curr.next

def reverse_group(array: list[ListNode], k: int):
    if len(array) < k:
        return array
    array.reverse()
    return array

def flatten(arrays):
    for array in arrays:
        for inner in array:
            yield inner

def re_linked(nodes):
    if not nodes:
        return None
    
    for index, curr_node in enumerate(nodes[:-1]):
        curr_node.next = nodes[index + 1]
    
    nodes[-1].next = None
    
    return nodes[0]


