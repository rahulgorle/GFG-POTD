class Solution:
    def printAllDups(self, root):
        ret = {}
        seen = set()
        def dfs(cur = root):
            if not cur:
                return [-1]
            left = dfs(cur.left)
            right = dfs(cur.right)
            tmp = [cur.data] + left + right
            if tuple(tmp) in seen:
                ret[tuple(tmp)] = cur
            else:
                seen.add(tuple(tmp))
            return tmp
        dfs()
        return [ret[x] for x in sorted(ret)]
