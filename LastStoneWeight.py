import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        x, y = 0, 0
        heapq.heapify_max(stones)
        while len(stones) > 1:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)
            if y - x > 0:
                heapq.heappush_max(stones, y-x)
        if not stones:
            return 0
        else:
            return heapq.heappop_max(stones)
