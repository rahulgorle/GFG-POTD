class Solution:
    # Function to check if a string can be obtained by rotating
    # another string by exactly 2 places.
    def isRotated(self, str1, str2):
        if len(str1) != len(str2):
            return False

        n = len(str1)

        # Check if string is rotated by 2 places clockwise
        clockwise_rotated = (str1[-2:] + str1[:-2])
        if clockwise_rotated == str2:
            return True

        # Check if string is rotated by 2 places anticlockwise
        anticlockwise_rotated = (str1[2:] + str1[:2])
        if anticlockwise_rotated == str2:
            return True

        return False
