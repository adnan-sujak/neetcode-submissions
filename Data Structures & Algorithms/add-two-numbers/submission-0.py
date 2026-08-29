# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        my_list = linked_list_to_arr(l1, l2)

        return arr_to_linked_list(my_list)


def loop_through_linked_list(l1: ListNode, l2: ListNode):

    curr1 = l1
    curr2 = l2

    while curr1 or curr2:
        yield (curr1.val if curr1 else 0), (curr2.val if curr2 else 0)
        curr1 = curr1.next if curr1 else None
        curr2 = curr2.next if curr2 else None


def linked_list_to_arr(l1: ListNode, l2: ListNode):
    my_list = []

    for node in loop_through_linked_list(l1, l2):
        my_list.append(node)

    result = []
    carry = 0

    for a, b in my_list:
        total = a + b + carry
        result.append(total % 10)
        carry = total // 10

    if carry:
        result.append(carry)

    return result


def arr_to_linked_list(my_list: list[int]):
    linked_result = [
        ListNode(node)
        for node in my_list
    ]

    for index, node in enumerate(linked_result):
        if index == len(linked_result) - 1:
            node.next = None
            continue
        node.next = linked_result[index + 1]

    return linked_result[0]