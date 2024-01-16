class Solution:
    def __init__(self):
        self.memo = {}

    def numberSequence(self, current_value, remaining_steps):
        # Check if the result is already memoized
        if (current_value, remaining_steps) in self.memo:
            return self.memo[(current_value, remaining_steps)]

        # Base case: if remaining steps are 0, return 1
        if remaining_steps == 0:
            return 1

        # Base case: if current value is less than remaining steps, return 0
        if current_value < remaining_steps:
            return 0

        # Recursive case: calculate the number sequence based on the given formula
        result = self.numberSequence(current_value - 1, remaining_steps) + \
                 self.numberSequence(current_value >> 1, remaining_steps - 1)

        # Memoize the result
        self.memo[(current_value, remaining_steps)] = result

        return result
