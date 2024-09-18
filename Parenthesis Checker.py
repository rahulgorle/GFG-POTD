class Solution:
    def ispar(self, x):
        stack = []
        matching_bracket = {')': '(', '}': '{', ']': '['}
        
        for char in x:
            if char in matching_bracket.values():
                stack.append(char)
            elif char in matching_bracket:
                if not stack or stack[-1] != matching_bracket[char]:
                    return False
                stack.pop()
        
        return not stack
