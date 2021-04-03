class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequent_words = {}
        for word in words:
            if word in frequent_words:
                frequent_words[word] += 1
            else:
                frequent_words[word] = 1

        heap = []
        for key in frequent_words:
            heapq.heappush(heap, (-frequent_words[key], key))

        res = []
        for i in range(k):
            popped = heapq.heappop(heap)
            res.append(popped[1])

        return res