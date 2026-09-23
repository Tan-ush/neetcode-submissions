class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        track = []
        for i, num in enumerate(sort):
            if i > 0 and sort[i] == sort[i - 1]:
                continue
            start = i + 1
            end = len(sort) - 1
            while start < end:
                sum = sort[i] + sort[start] + sort[end]
                if sum == 0:
                    track.append([sort[i], sort[start], sort[end]])
                    start += 1
                    while sort[start] == sort[start - 1] and start < end:
                        start += 1
                elif sum < 0:
                    start += 1
                else:
                    end -= 1
        return track


                
                





        