class TrieNode:
    def __init__(self):
        self.childNodes = {}
        self.eow = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c in cur.childNodes:
                cur = cur.childNodes[c]
            else:
                cur.childNodes[c] = TrieNode()
                cur = cur.childNodes[c]
        cur.eow = True

    def search(self, word: str) -> bool:
        '''
            for each char, trace down to tree. If ".", explore all child nodes, with dfs.
            dfs can be done with recursion
        '''
        # need to track cur, outside of recursion
        def dfs(word, cur) -> bool:
            # termination
            if len(word) == 0:
                return cur.eow

            c = word[0]
            if c == ".":
                for child in cur.childNodes:
                    if dfs(word[1:], cur.childNodes[child]):
                        return True
                return False
            else:
                if c in cur.childNodes:
                    return dfs(word[1:], cur.childNodes[c])
                else:
                    return False
            
        cur = self.root
        return dfs(word, cur)