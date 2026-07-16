class Solution:
    def reverseBits(self, n: int) -> int:
        '''
            Core idea:
                1. Scan from right to left.
                2. Move bits from rightmost to old leftmost
                3. bit count 0 start from the rightmost bit
            Algo:
                1. Can use a res bit to store
                2. For optimal space complexity, update n in-place

        '''
        res = 0
        for i in range(32):
            # extract the rightmost bit
            bit = (n >> i) & 1
            res |= bit << (31 - i)
        return res