class TrieNode:
    def __init__(self):
        self.child = {}
        self.eow = False

class PrefixTree:
    '''
        Should define Nodes, similar to Lined List, where each Node points to its child Nodes.
        Can use dict, key for node, value for child nodes.
    '''

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root     # start from root

        for c in word:
            if c in cur.child:
                cur = cur.child[c]
            else:
                cur.child[c] = TrieNode()
                cur = cur.child[c]
        cur.eow = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c in cur.child:
                cur = cur.child[c]
            else:
                return False
        
        if cur.eow:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c in cur.child:
                cur = cur.child[c]
            else:
                return False
        
        return True
        
        