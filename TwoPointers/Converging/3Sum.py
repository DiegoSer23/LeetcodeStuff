class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l_ptr, r_ptr = i + 1, n - 1
            while l_ptr < r_ptr:
                current_sum = nums[i] + nums[l_ptr] + nums[r_ptr]
                if current_sum < 0:
                    l_ptr += 1
                elif current_sum > 0:
                    r_ptr -= 1
                else:
                    result.append([nums[i], nums[l_ptr], nums[r_ptr]])
                    l_ptr += 1
                    while nums[l_ptr] == nums[l_ptr-1] and l_ptr < r_ptr:
                        l_ptr += 1
        return result
