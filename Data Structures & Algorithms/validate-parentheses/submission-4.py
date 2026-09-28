class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {"]":"[", "}": "{", ")":"("}
        opening = ("(", "[", "{")

        for k in s:
            if k in opening:
                stack.append(k)
            else:
                if len(stack) > 0:
                    top = stack.pop()
                    if not top == match[k]:
                        return False
                else:
                    return False
        return len(stack) == 0

        