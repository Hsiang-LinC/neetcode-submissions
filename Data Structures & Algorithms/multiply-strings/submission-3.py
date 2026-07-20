class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
            Multiplication digit-by-digit.
            Carries are divided by 10, and added to the next digit.
        '''
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        res = ["0"] * (m + n)
        for i in range(m - 1, -1, -1):
            carry = 0
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j]) + int(res[i+j+1])
                res[i+j+1] = str(mul % 10)
                res[i+j] = str(int(res[i+j]) + mul // 10)
                carry = int(res[i+j])
        if carry:
            res[0] = str(carry)
            return "".join(res)
        else:
            return "".join(list(res)[1:])