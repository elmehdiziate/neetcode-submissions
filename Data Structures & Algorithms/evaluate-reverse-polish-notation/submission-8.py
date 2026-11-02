class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            result = 0
            if t in ["+","-","*","/"]:
                n1 = stack.pop()
                n2 = stack.pop()
                if t == "+":
                    stack.append(n2 + n1)
                elif t == "-":
                    stack.append(n2 - n1)
                elif t == "*":
                    stack.append(n2 * n1)
                elif t == "/":
                    stack.append(int(n2 / n1))
            else:
                stack.append(int(t))
        return stack[0]
