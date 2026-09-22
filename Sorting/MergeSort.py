class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def mergeSort(nums: list[int]):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left_nums = nums[:mid]
            right_nums = nums[mid:]
            sortedL = mergeSort(left_nums)
            sortedR = mergeSort(right_nums)
            return merge(sortedL, sortedR)
        def merge(sorted_L, sorted_R):
            result = []
            i = j = 0
            while i < len(sorted_L) and j < len(sorted_R):
                if sorted_L[i] < sorted_R[j]:
                    result.append(sorted_L[i])
                    i += 1
                else:
                    result.append(sorted_R[j])
                    j += 1
            result.extend(sorted_L[i:])
            result.extend(sorted_R[j:])
            return result
        return mergeSort(nums)
