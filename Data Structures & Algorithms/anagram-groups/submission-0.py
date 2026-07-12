class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            res[sorted_str].append(s)
        return list(res.values())