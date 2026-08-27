# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        for node in self.for_each_node(head):
            if node in visited:
                return True
            visited.add(node)
        return False


    def for_each_node(self, head:ListNode):
        curr = head

        while curr is not None:
            yield curr
            curr = curr.next