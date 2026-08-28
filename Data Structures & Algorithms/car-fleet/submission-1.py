class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
            stack that the ttd must be in decreasing order
        '''
        ttd = [0] * len(position)
        for i in range(len(position)):
            ttd[i] = (target - position[i]) / speed[i]
        pair = [[p, t] for p, t in zip(position, ttd)]
        pair = sorted(pair)

        q = []
        for i in range(len(pair)):
            while q and pair[i][1] >= q[-1][1]:
                q.pop()
            q.append(pair[i])
        return len(q)