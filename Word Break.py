class Solution:
    def wordBreak(self, input_string, word_dict):
        def wordBreakUtil(s, word_dict):
            if not s:
                self.result = 1
                return
       
            temp, pos = "", 1
            for i in s:
                temp += i
                if temp in word_dict:
                    wordBreakUtil(s[pos:], word_dict)
                pos += 1
       
        self.result = 0
        wordBreakUtil(input_string, word_dict)
        return self.result
