class Solution:
    def firstElement (self, n):
        first_element = 1
        second_element = 1
        res = 0
        if n <= 2:
            return first_element
        for i in range(3,n+1):
            res = (first_element+second_element)%1000000007
            first_element = second_element
            second_element = res
        return res
