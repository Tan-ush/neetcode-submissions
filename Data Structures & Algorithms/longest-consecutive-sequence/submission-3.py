class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums:
            longest = 1
        else:
            longest = 0
        dict = {}
        for i, num in enumerate(nums):
            dict[num] = True
        for n in nums:
            cur = n
            long = 1
            next = True
            if dict.get(cur - 1):
                continue
            while next:
                next = False
                if dict.get(cur + 1):
                    next = True
                    cur += 1
                    long += 1
            if long > longest:
                longest = long
        return longest
                
                


            


        