class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if dict.get(nums[i]) == None:
                dict[nums[i]] = [i]
            else:
                dict[nums[i]].append(i)
        for i in range(len(nums)):
            other = target - nums[i]
            if dict.get(other) is not None:
                if other == nums[i] and len(dict[other]) > 1:
                    return [dict[nums[i]][0], dict[nums[i]][1]]
                elif nums[i] != other:
                    return [dict[nums[i]][0], dict[other][0]]