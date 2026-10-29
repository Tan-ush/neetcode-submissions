class Solution:
    def isValid(self, s: str) -> bool:
        map = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch not in map:
                stack.append(ch)
            else:
                if not stack:
                    return False
                opp = stack.pop()
                if map[ch] != opp:
                    return False
        if stack:
            return False
        return True


        