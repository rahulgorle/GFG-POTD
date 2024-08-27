from collections import deque
class Solution:
    def findMaxDiff(self, arr):
        ls = deque()
        stack = [0,arr[0]] #candidate map karne ke liye ki aage kaam aaega ya nahii
        
        for i in range(1,len(arr)):
            
            if arr[i-1]<arr[i]:
                ls.append(arr[i-1])
                stack.append(arr[i])
            else:
                while stack[-1]>= arr[i]:
                    stack.pop()
                
                ls.append(stack[-1])
                stack.append(arr[i])
        ls.appendleft(0)
                
        rs = deque()
        arr.reverse()
        stack =  [0,arr[0]]
        for i in range(1,len(arr)):
            if arr[i-1]<arr[i]:
                rs.append(arr[i-1])
                stack.append(arr[i])
            else:
                while stack[-1]>= arr[i]:
                    stack.pop()
                
                rs.append(stack[-1])
                stack.append(arr[i])
        rs.appendleft(0)
        rs.reverse()
        
        diff = 0
        
        for i in range(len(arr)):
            diff = max(diff,abs(ls[i]-rs[i]))
        return diff
