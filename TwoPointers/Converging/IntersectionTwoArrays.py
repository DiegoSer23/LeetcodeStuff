class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        array_set = set()
        res = set()
        for i in range(len(nums1)):
            if nums1[i] not in array_set:
                array_set.add(nums1[i])
        for j in range(len(nums2)):
            if nums2[j] in array_set:
                res.add(nums2[j])
        return list(res)
