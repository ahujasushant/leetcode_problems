# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        arr = []
        for i in lists:
            while i:
                heapq.heappush(arr, i.val)
                i = i.next
        result = []
        while arr:
            result.insert(0,heappop(arr))
        resultNode = None
        for i in result:
            resultNode = ListNode(i, resultNode)
        return resultNode