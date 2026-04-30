class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = { "}":"{", "]": "[", ")":"(" }
        for ch in s :
            if ch in "{[(" :
                stack.append(ch)
            else :
                if len(stack) == 0 :
                    return False
                if match[ch] == stack[-1] :
                    stack.pop(-1)
                else:
                    return False
        if len(stack) == 0 :
            return True
        return False