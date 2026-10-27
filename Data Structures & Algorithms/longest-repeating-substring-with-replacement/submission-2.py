from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = defaultdict(int)
        cur = s[0]
        max_freq = 0


        for i in range(len(s)):
            count[s[i]] += 1
            max_freq = max(max_freq, count[s[i]])
            while (i - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, i - l + 1)
        return res

        


            
        


        