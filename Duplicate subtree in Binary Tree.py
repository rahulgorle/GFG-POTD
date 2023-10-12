class Solution:
    def dfs(self, root, d, ans):
        if root == None: return '#'
        left  = self.dfs(root.left, d, ans)
        right = self.dfs(root.right, d, ans)
        key = str(root.data) + '|' + left + '|' + right
        if root.left != None and root.right != None:
            if key in d: ans[0] = True
        d[key] = True
        return key

    def dupSub(self, root):
        d = dict()
        ans = [False]
        self.dfs(root, d, ans)
        return 1 if ans[0] else 0
