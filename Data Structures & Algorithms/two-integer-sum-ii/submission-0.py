class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        e = len(numbers) - 1
        cur = numbers[i] + numbers[e]
        while cur != target:
            if cur < target:
                i += 1
            else:
                e -= 1
            cur = numbers[i] + numbers[e]
        return [i + 1, e + 1]
            
        