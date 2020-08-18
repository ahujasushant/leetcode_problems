# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_head = l1
        l2_head = l2
        new_l3 = None
        l3_last_node = None
        while l1_head and l2_head:
            if l1_head.val < l2_head.val:
                data_to_add = l1_head.val
                l1_head = l1_head.next
            else:
                data_to_add = l2_head.val
                l2_head = l2_head.next
            if new_l3 is None:
                new_l3 = ListNode(data_to_add, None)
                l3_last_node = new_l3
            else:
                l3_last_node.next = ListNode(data_to_add, None)
                l3_last_node = l3_last_node.next
        while l1_head:
            if new_l3 is None:
                new_l3 = ListNode(l1_head.val, None)
                l3_last_node = new_l3
            else:
                l3_last_node.next = ListNode(l1_head.val, None)
                l3_last_node = l3_last_node.next
            l1_head = l1_head.next
            
        while l2_head:
            if new_l3 is None:
                new_l3 = ListNode(l2_head.val, None)
                l3_last_node = new_l3
            else:
                l3_last_node.next = ListNode(l2_head.val, None)
                l3_last_node = l3_last_node.next
            l2_head = l2_head.next
        return new_l3
