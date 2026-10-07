class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
            build adjacency graph, where each node is connected by same pattern.
            pattern: only one different char
        '''
        if endWord not in wordList or beginWord == endWord:
            return 0
        wordLen = len(beginWord)
        pat = collections.defaultdict(set)
        
        for word in wordList:
            for i in range(wordLen):
                pattern = word[:i] + '*' + word[i+1:]
                pat[pattern].add(word)
        
        q = collections.deque([beginWord])
        visited = set()
        res = 0
        
        while q:
            res += 1
            for _ in range(len(q)):
                word = q.popleft()
                visited.add(word)
                
                if word == endWord:
                    return res

                for i in range(wordLen):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nxt in pat[pattern]:
                        if nxt not in visited:
                            q.append(nxt)
        
        return 0
