# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr_node = head
        while curr_node:
            if curr_node.next is None: break
            if curr_node.val == curr_node.next.val:
                curr_node.next = curr_node.next.next
                curr_node = curr_node
                continue
            curr_node = curr_node.next
        return head
