class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        freq = [[] for i in range(len(nums)+1)]
        res = []
        for e in nums:
            elements[e] = elements.get(e, 0) + 1
        for key, value in elements.items():
            freq[value].append(key)
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
