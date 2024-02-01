class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for alphabet in alphabets:
            if alphabet not in s.lower():
                return 0
        else:
            return 1
