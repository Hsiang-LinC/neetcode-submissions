class Solution:
    def __init__(self):
        self.num2Char = {"2": "abc",
                         "3": "def",
                         "4": "ghi",
                         "5": "jkl",
                         "6": "mno",
                         "7": "pqrs",
                         "8": "tuv",
                         "9": "wxyz"}
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        path = []
        def dfs(i):
            if i == len(digits):
                res.append("".join(path))
                return
            
            for c in self.num2Char[digits[i]]:
                path.append(c)
                dfs(i+1)
                path.pop()
                
        if not digits:
            return []
        dfs(0)
        return res