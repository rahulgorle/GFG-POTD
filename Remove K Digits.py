class Solution:
    def removeKdigits(self, num_str, k):
        digit_stack = []
       
        for current_digit in num_str:
            while digit_stack and k > 0 and current_digit < digit_stack[-1]:
                k -= 1
                digit_stack.pop()
           
            digit_stack.append(current_digit)
       
        while k > 0:
            digit_stack.pop()
            k -= 1
       
        return "".join(digit_stack).lstrip('0') or '0'
