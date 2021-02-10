# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        sorted_list_node = None
        sorted_list = []
        while head:
            heapq.heappush(sorted_list, head.val)
            head = head.next
        h = []
        for i in range(len(sorted_list)):
            h.append(heappop(sorted_list))
        for i in h[::-1]:
            sorted_list_node = ListNode(i, sorted_list_node)
        return sorted_list_node

