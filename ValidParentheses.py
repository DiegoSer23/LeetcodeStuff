class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] in ("(", "{", "["):
                stack.append(s[i])
            elif s[i] in (")", "}", "]") and not stack:
                return False
            elif s[i] == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    break
            elif s[i] == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    break
            elif s[i] == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    break
        
        if not stack:
            return True
        else:
            return False
