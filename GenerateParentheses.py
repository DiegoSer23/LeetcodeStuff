class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(left_count: int, right_count: int, current_string: str):
            if left_count > n or right_count > n or left_count < right_count:
                return
            
            if left_count == n and right_count == n:
                result.append(current_string)
                return
            
            backtrack(left_count + 1,  right_count, current_string + "(")
            backtrack(left_count, right_count + 1, current_string + ")")
        result = []
        backtrack(0,0, "")
        return result
