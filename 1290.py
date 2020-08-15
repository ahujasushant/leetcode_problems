# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary_number_str = 
        curr_node = head
        while curr_node:
            binary_number_str += str(curr_node.val)
            curr_node = curr_node.next
        integer = 0
        for i in binary_number_str:
            integer = (2*integer) + int(i)
        return integer
