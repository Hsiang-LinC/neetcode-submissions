class TrieNode:
    def __init__(self):
        self.child = {}
        self.isWord = False
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
            use a trie struction to check if next word is in the child nodes
        '''
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        Row, Col = len(board), len(board[0])
        res = []
        path = []
        visited = set()

        def dfs(r, c, node):
            if (r < 0 or c < 0 or
                r >= Row or c >= Col or
                (r, c) in visited or
                board[r][c] not in node.child):
                return
            
            nextChar = board[r][c]
            nextNode = node.child[nextChar]
            path.append(nextChar)
            visited.add((r, c))

            if nextNode.isWord:
                res.append("".join(path))
                nextNode.isWord = False

            dfs(r, c + 1, nextNode)
            dfs(r, c - 1, nextNode)
            dfs(r + 1, c, nextNode)
            dfs(r - 1, c, nextNode)

            path.pop()
            visited.remove((r, c))
        
        for i in range(Row):
            for j in range(Col):
                dfs(i, j, root)
        
        return res
        
        