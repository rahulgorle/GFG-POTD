class Solution:
    def nthCharacter(self, s, r, n):
        if n==0:
            return s[0]
        for i in range(r):
            temp=""
            for j in range(n//2 +1):
                if s[j]=="0":
                    temp+="01"
                else:
                    temp+="10"
            s=temp[:]
        return s[n]
