# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        last_node = head
        prev = None
        while last_node:
            if head.val == val:
                head = head.next
                last_node = head
                continue
            if last_node.val == val:
                last_node = last_node.next
                prev.next = last_node
                continue
            prev = last_node
            last_node = last_node.next
        return head
