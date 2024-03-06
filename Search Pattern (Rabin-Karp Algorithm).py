class Solution:
    def search(self, pattern, text):
        p = 11
        add = 0
        for c in pattern:
            add+=ord(c)
        patternhash = add%p
        add = 0
        for i in range(len(pattern)):
            add+=ord(text[i])
        initialhash = add%p
        i = 0
        j = len(pattern)-1
        ans = []
        while(j<len(text)):
            # print(text[i:j+1],"text")
            if(initialhash == patternhash):
                if(pattern == text[i:j+1]):
                    ans.append(i+1)
            add-=ord(text[i])
            if(j+1<len(text)):
                add+=ord(text[j+1])
            initialhash = add%p
            j+=1
            i+=1
        return ans
