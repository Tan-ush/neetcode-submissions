class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = i
            other = target - nums[i]
            if other in dict and dict[other] != i:
                return [dict[other], i]
        