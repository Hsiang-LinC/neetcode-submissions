class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
            maintain a queue of indices, where the temp value is decreasing
            pop value lower than new temp
            update result list when pop 
        '''
        res = [0] * len(temperatures)
        q = []

        for i, t in enumerate(temperatures):
            while q and temperatures[q[-1]] < t:
                res_id = q.pop()
                res[res_id] = i - res_id
            q.append(i)
        return res