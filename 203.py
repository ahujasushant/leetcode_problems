# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr_node = head
        last_node = head
        prev = None
        while last_node:
            if curr_node.val == val:
                curr_node = curr_node.next
                last_node = curr_node
                continue
            if last_node.val == val:
                last_node = last_node.next
                prev.next = last_node
                continue
            prev = last_node
            last_node = last_node.next
        return curr_node
