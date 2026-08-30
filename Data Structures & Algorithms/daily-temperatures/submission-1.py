class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
            use stack to track index of a monotoic decreasing list
            stack q track the indices, not temperature values
        '''
        q = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while q and temperatures[i] > temperatures[q[-1]]:
                k = q.pop()
                res[k] = i - k
            q.append(i)
        return res