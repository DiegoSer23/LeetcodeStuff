class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            while j < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, low, high):
            if low == high:
                return arr
            mid = (low+high) // 2
            mergeSort(arr,low,mid)
            mergeSort(arr,mid+1,high)
            merge(arr,low,mid,high)
            return arr
        return mergeSort(nums, 0, len(nums)-1)
