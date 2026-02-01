class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        count = 0
        res = 0
        n = len(s)
        for i in range(n):
            if res >= n - i:
                break
            seen.add(s[i])
            count += 1
            for j in range(i + 1, n):
                if s[j] not in seen:
                    seen.add(s[j])
                    count += 1
                else:
                    break
            seen.clear()
            res = max(res, count)
            count = 0
        return res
