class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l_idx, r_idx, = 0, len(nums) - 1
        while l_idx <= r_idx:
            m_idx =  (r_idx + l_idx) // 2
            if nums[m_idx] == target:
                return m_idx
            if target < nums[m_idx]:
                r_idx = m_idx - 1
            else:
                l_idx = m_idx + 1
        if target <= nums[m_idx]:
            return m_idx
        else:
            return m_idx + 1
