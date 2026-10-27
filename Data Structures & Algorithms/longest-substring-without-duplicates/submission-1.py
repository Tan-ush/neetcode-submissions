class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        best = 0
        l = 0
        r = 0
        for i in range(len(s)):
            if s[i] in seen:
                best = max(best, r - l)
                last = seen[s[i]]
                while l != last + 1:
                    del seen[s[l]]
                    l += 1
            seen[s[i]] = i
            r += 1
            
        best = max(best, r - l)
        return best



        