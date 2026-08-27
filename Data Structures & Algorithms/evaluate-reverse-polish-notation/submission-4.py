class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
            need to operate on previous 2 numbers
            a data structure to keep track of
        '''
        s = []
        for t in tokens:
            if t == "+":
                b = s.pop()
                a = s.pop()
                s.append(a + b)

            elif t == "-":
                b = s.pop()
                a = s.pop()
                s.append(a - b)

            elif t == "*":
                b = s.pop()
                a = s.pop()
                s.append(a * b)

            elif t == "/":
                b = s.pop()
                a = s.pop()
                s.append(int(a / b))

            else:
                s.append(int(t))

        return s[0]