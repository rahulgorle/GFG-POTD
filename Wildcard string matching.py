class Solution:
    def match(self, wild, pattern):
        # code here

        meta = lambda c: c == '?' or c == '*'
        
        def ok(wild, pattern):
            if not wild and not pattern:
                return True
            if not wild or not pattern:
                return False
            if not meta(wild[0]):
                if wild[0] != pattern[0]:
                    return False
                return ok(wild[1:], pattern[1:])
            elif wild[0] == '?':
                return ok(wild[1:], pattern[1:])
            else:
                for i in range(len(pattern)+1):
                    if ok(wild[1:], pattern[i:]):
                        return True
                return False
        return ok(wild, pattern)
