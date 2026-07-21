class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
            Need to encode length, but also aware of string containing numbers.
            Use num# in between.
        '''
        enc = ""
        for s in strs:
            enc = enc + str(len(s)) + '#' + s     # "str1
            
        return enc

    def decode(self, s: str) -> List[str]:
        dec: list[str] = []

        acc_len = 0
        while acc_len < len(s):
            d_len = 0
            while s[acc_len] != '#':
                d_len += 1
                acc_len += 1
            w_len = int(s[acc_len-d_len:acc_len])
            dec.append(s[acc_len+1:acc_len+1+w_len])
            acc_len += 1 + w_len

        return dec