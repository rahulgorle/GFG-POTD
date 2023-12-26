from typing import List
from typing import List
class Solution:
    def sumZeroMatrix(self, a : List[List[int]]) -> List[List[int]]:
        m,n=len(a),len(a[0])
        pre_sum=[[0]*(n+1) for _ in range(m+1)]
        def solve(arr):
            mp={0:-1}
            ssum=0
            l,r=-1,-1
            for i,val in enumerate(arr):
                ssum=ssum+val
                if ssum in mp:
                    ll,rr=mp[ssum],i
                    if rr-ll>r-l:
                        l,r=ll,rr
                else:
                    mp[ssum]=i
            return l+1,r
        for i in range(1,m+1):
            for j in range(1,n+1):
                pre_sum[i][j]=pre_sum[i][j-1]+a[i-1][j-1]
        lr,rr,lc,rc,ans=-1,-1,-1,-1,0
        for c1 in range(1,n+1):
            for c2 in range(c1,n+1):
                arr=[]
                for i in range(1,m+1):
                    arr.append(pre_sum[i][c2]-pre_sum[i][c1-1])
                l,r=solve(arr)
                if l==r==-1: continue
                if (r-l+1)*(c2-c1+1)>ans:
                    lr,rr=l,r
                    lc,rc=c1-1,c2-1
                    ans=(r-l+1)*(c2-c1+1)
                elif (r-l+1)*(c2-c1+1)==ans and lc==c1:
                    if l<lr:
                        lr,rr=l,r
                        lc,rc=c1-1,c2-1
                        ans=(r-l+1)*(c2-c1+1)
                    elif l==lr and r>rr:
                        lr,rr=l,r
                        lc,rc=c1-1,c2-1
                        ans=(r-l+1)*(c2-c1+1)
        ret=[] 
        # print(lr,rr,lc,rc,ans)
        if ans==0:
            return ret
        for i in range(lr,rr+1):
            tt=[]
            for j in range(lc,rc+1):
                tt.append(a[i][j])
            ret.append(tt)
        return ret
        

