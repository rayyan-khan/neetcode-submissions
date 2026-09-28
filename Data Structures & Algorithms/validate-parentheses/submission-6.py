class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stacklen = 0
        match = {"]":"[", "}": "{", ")":"("}
        opening = ("(", "[", "{")


        for k in s:
            if k in opening:
                stack.append(k)
                stacklen += 1
            else:
                if stacklen > 0:
                    if not stack.pop() == match[k]:
                        return False
                    stacklen -= 1
                else:
                    return False
        return stacklen == 0

        