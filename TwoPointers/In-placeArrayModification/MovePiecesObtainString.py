class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        start_idx = 0
        target_idx = 0
        while target_idx < n or start_idx < n:
            while target_idx < n and target[target_idx] == "_":
                target_idx += 1
            while start_idx < n and start[start_idx] == "_":
                start_idx += 1
            if start_idx == n or target_idx == n:
                return start_idx == n and target_idx == n
            if target[target_idx] != start[start_idx]:
                return False
            elif target[target_idx] == "L" and start_idx < target_idx:
                return False
            elif target[target_idx] == "R" and start_idx > target_idx:
                return False
            start_idx += 1
            target_idx += 1
        return True
