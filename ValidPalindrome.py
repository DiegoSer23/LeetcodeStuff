import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        lindx, rindx = 0, len(clean_str)-1
        if len(clean_str) == 0:
            return True
        while lindx <= rindx:
            if clean_str[lindx] == clean_str[rindx]:
                lindx += 1
                rindx -= 1
            else:
                return False
        return True
