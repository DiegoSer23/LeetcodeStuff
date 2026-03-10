class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heap = [num for num in target]
        heapify_max(heap)
        total_sum = sum(target)
        while heap[0] > 1:
            cur_sum = heappop_max(heap)
            sum_others = total_sum - cur_sum
            if sum_others == 0 or cur_sum - sum_others < 1:
                return False
            prev_value = (cur_sum % sum_others) or sum_others
            heappush_max(heap, prev_value)
            total_sum = total_sum - cur_sum + prev_value
        return True
