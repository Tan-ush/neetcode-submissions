class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            if dict.get(i) == None:
                dict[i] = 1
            else: 
                dict[i] += 1
            if dict[i] > 1:
                return True
        return False