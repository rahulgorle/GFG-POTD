class Solution:
    def generateSubsequences(self, s, index, current, result):
        if index == len(s):
            if current:
                result.append(current)
            return
        
        # Include the current character
        self.generateSubsequences(s, index + 1, current + s[index], result)
        
        # Exclude the current character
        self.generateSubsequences(s, index + 1, current, result)
    
    def AllPossibleStrings(self, s):
        result = []
        self.generateSubsequences(s, 0, '', result)
        result.sort()  # Sort the result lexicographically
        return result
