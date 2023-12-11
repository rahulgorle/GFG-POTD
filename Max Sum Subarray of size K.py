class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        a =0 
        for i in range(0,K):
            a+=Arr[i]
        
        cur=a
        for i in range(K,N):
            cur+=Arr[i]-Arr[i-K]
            a=max(a,cur)
        
        return a
