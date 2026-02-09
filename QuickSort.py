def partition(self, nums, low, high):
        i = low - 1
        pivot = nums[high]
        for j in range(low,high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[high] = nums[high], nums[i+1]
        return i + 1

    def quickSort(self, nums, low=0, high=None):
        if high is None:
            high = len(nums) - 1
        if low < high:
            p_idx = self.partition(nums, low, high)
            self.quickSort(nums, low, p_idx-1)
            self.quickSort(nums, p_idx+1, high)
