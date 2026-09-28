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
                    if not stack.pop() == match[k]:
                        return False
                else:
                    return False
        return len(stack) == 0

        