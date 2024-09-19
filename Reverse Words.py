class Solution:
    def reverseWords(self, str):
        out = ''
        word = str.split('.')
        for i in range(len(word)-1, 0, -1):
            item = word[i] + '.'
            out = out + item
        out = out + word[0]
        return out
