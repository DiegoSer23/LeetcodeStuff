class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if len(count) <= 2:
                continue
            new_count = defaultdict(int)
            for key, c in count.items():
                if c > 1:
                    new_count[key] = c - 1
            count = new_count
        res = []
        for c in count:
            if nums.count(c) > len(nums) // 3:
                res.append(c)
        return res
