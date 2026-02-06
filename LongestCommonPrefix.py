class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = 0
        common = True
        while common:
            if idx >= len(strs[0]):
                break
            compare = strs[0][idx]
            for value in strs:
                if idx >= len(value) or compare != value[idx]:
                    common = False
                    break
            if common: idx += 1
        return strs[0][0:idx]
