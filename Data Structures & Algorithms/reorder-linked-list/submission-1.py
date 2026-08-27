# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        if head is None:
            return None
        
        original_values = list(self.loop_through(head))
        
        front = True
        reordered = []
        while original_values:
            if front:
                reordered.append(original_values.pop(0))
            else:
                reordered.append(original_values.pop())
            front = not front
        self.to_linked_list(reordered)
        return

    def to_linked_list(self, nodes):

        for index, node in enumerate(nodes):
            if index == len(nodes) - 1:
                node.next = None
                continue
            node.next = nodes[index + 1]
        return nodes[0]


    def loop_through(self, head: ListNode):

        curr = head

        while curr is not None:
            yield curr
            curr = curr.next

