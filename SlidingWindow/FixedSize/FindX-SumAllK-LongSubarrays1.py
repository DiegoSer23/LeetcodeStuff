import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ocurrences = {}
        n = len(nums)
        res = []
        for i in range(n):
            if nums[i] not in ocurrences:
                ocurrences[nums[i]] = 1
            else:
                ocurrences[nums[i]] += 1
            if i >= k - 1:
                if i >= k:
                    ocurrences[nums[i-k]] -= 1
                top_values = heapq.nlargest(x, ocurrences.items(),  key=lambda item: (item[1], item[0]))
                count = 0
                for j in range(len(top_values)):
                    m_key, m_val = top_values[j]
                    count += m_key * m_val
                res.append(count)
        return res
