class Solution:
    def KDistance(self,root,k):
        queue=[]
        ans=[]
    
        count=0
        queue.append(root)
        while queue and count<=k+1:
            level=[]
            for i in range(len(queue)):
                node=queue.pop(0)
                if node:
                    level.append(node.data)
                    queue.append(node.left)
                    queue.append(node.right)
    
            if level:
                ans.append(level)
                count+=1
    
        return ans[k] if len(ans)>k else []
