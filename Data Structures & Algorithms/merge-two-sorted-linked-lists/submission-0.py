# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        array1 = self.linkedListToArray(list1)
        array2 = self.linkedListToArray(list2)

        joined_list = array1 + array2

        joined_list.sort()

        return self.arrayToLinkedList(joined_list)


    def linkedListToArray(self, list1: Optional[ListNode]) -> list[int] :
        new_list=[]
        if list1 is None:
            return []
        
        for numbers in loop_through_linked_list(list1):
            new_list.append(numbers)
        return new_list
    
    def arrayToLinkedList(self, arr: list[int]) -> Optional[ListNode]:
        if not arr:
            return None
        
        nodes = [
            ListNode(val)
            for val in arr
        ]

        for index, node in enumerate(nodes):
            if index == len(nodes) - 1:
                continue
            node.next = nodes[index + 1]

        return nodes[0]


def loop_through_linked_list(head: ListNode):
    curr = head

    while curr is not None:
        yield curr.val
        curr = curr.next




        