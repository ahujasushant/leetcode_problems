# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr_node = head
        if curr_node is None:
            new_curr_node = None
            return new_curr_node
        else:
            new_curr_node = ListNode(curr_node.val, None)
        while curr_node.next:
            new_curr_node = ListNode(curr_node.next.val, new_curr_node)
            curr_node = curr_node.next
        return new_curr_node
