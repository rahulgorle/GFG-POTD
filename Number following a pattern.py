class Solution:
    def printMinNumberForPattern(self, S):
        result = []
        temp_stack = []
        current_num = 1

        for char in S:
            if char == "D":
                temp_stack.append(current_num)
                current_num += 1
            else:
                temp_stack.append(current_num)
                current_num += 1
                # Convert to str and reverse the temp_stack
                # Add to result and reset temp_stack
                result += [str(i) for i in temp_stack][::-1]
                temp_stack = []

        temp_stack.append(current_num)
        result += [str(i) for i in temp_stack][::-1]

        return int(''.join(result))
