class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # if more than two 0's final is useless
        product = 1
        flag = 0
        for num in nums:
            if num == 0:
                flag += 1
                continue
            product *= num
        
        if flag > 1:
            return [0] * len(nums)
        elif flag == 1:
            final = [0] * len(nums)
        else:
            final = [1] * len(nums)
        
        for i, n in enumerate(nums):
            if n == 0:
                final[i] = product
            else:
                final[i] = final[i] * product//n
        return final

        

            
        
