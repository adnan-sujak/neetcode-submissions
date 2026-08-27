# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        new_list = list(loop_through_linked_list(head))

        new_list.pop(-n)

        if not new_list:
            return None

        relink(new_list)

        return new_list[0]


def relink(nodes: list[ListNode]):
    for index, node in enumerate(nodes):
        is_last = index == len(nodes) - 1
        node.next = None if is_last else nodes[index + 1]
                


def loop_through_linked_list(head: ListNode):
    curr = head

    while curr:
        yield curr
        curr = curr.next