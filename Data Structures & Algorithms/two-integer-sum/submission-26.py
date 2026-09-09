class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            other = target - nums[i]
            if other in dict and dict[other] != i:
                return [dict[other], i]
            dict[nums[i]] = i