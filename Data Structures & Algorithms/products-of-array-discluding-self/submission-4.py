class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # if more than two 0's final is useless
        product = 1
        flag = False
        
        for num in nums:
            if num == 0 and not flag:
                flag = True
                continue
            product *= num
        
        if flag:
            final = [0] * len(nums)
        else:
            final = [1] * len(nums)
        
        for i, n in enumerate(nums):
            if n == 0:
                final[i] = product
            else:
                final[i] = final[i] * product//n
        return final

        

            
        
