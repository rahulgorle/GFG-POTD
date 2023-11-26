class Solution:
    def pattern(self, N):
        result = [N]
        new_value = N
        
        # Generating the decreasing sequence until new_value becomes greater than 0
        while new_value > 0:
            new_value -= 5
            result.append(new_value)
        
        # Generating the increasing sequence until new_value regains its initial value
        while new_value != N:
            new_value += 5
            result.append(new_value)
        
        return result
