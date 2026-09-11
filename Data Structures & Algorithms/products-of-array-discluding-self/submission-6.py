class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = [1] * len(nums)
        pre = 1
        for i in range(len(nums)):
            final[i] *= pre
            pre *= nums[i]
            # 1, 1, 2, 6

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            final[i] *= post
            post *= nums[i]
            # _  12 6 
        return final


        

            
        
