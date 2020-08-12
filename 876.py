# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        node_one = head
        node_one_count = 0
        node_two = head
        node_two_count = 0
        while node_two.next is not None:
            if node_two.next.next is None:
                node_one_count += 1
                break
            node_two_count += 2
            node_one_count += 1
            node_two = node_two.next.next
            node_one = node_one.next
        if node_one.next is None: return node_one
        if (node_two_count < node_one_count) or (node_two_count == node_one_count): 
            return node_one.next
        if node_two_count % node_one_count == 0:
            return node_one
        return node_one.next
