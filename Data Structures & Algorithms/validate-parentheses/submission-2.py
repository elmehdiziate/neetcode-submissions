class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        result = False
        par = ["[","{","("]
        for c in s:
            if c in par:
                stack.append(c)
            else:
                if stack == []:
                    return False
                ch = stack.pop()
                if (ch == "[" and c == "]") or (ch == "{" and c == "}") or (ch == "(" and c == ")"):
                    result = True
                else:
                    return False
        if stack != [] :
            return False
        return result
            

        