class Solution:
    def smallestSubstring(self, input_string):
        last_occurrence = [-1] * 128
        string_length = len(input_string)
        minimum_length = float('inf')

        for current_index in range(string_length):
            last_occurrence[ord(input_string[current_index])] = current_index
            min_occurrence = min(last_occurrence[ord(char)] for char in input_string[:current_index + 1])
            if min_occurrence != -1:
                minimum_length = min(minimum_length, current_index - min_occurrence + 1)

        return -1 if minimum_length == float('inf') else minimum_length
