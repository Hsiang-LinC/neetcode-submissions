class Solution:
    def isValid(self, s: str) -> bool:
        '''
            LIFO
        '''
        q = collections.deque()
        
        for c in s:
            if c in {'(', '{', '['}:
                q.append(c)
            elif q and (
            (c == ')' and q[-1] == '(')
            or (c == '}' and q[-1] == '{') 
            or (c == ']' and q[-1] == '[')):
                q.pop()
            else:
                return False
        
        return False if q else True
            