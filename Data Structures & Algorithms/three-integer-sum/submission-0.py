class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        track = []
        for i, num in enumerate(sort):
            start = 0
            end = len(sort) - 1
            while start < end:
                if start == i:
                    start += 1
                    continue
                if end == i:
                    end -= 1
                    continue
                sum = sort[i] + sort[start] + sort[end]
                if sum == 0 and sorted([sort[i], sort[start], sort[end]]) not in track:
                    track.append(sorted([sort[i], sort[start], sort[end]]))
                if sum < 0:
                    start += 1
                else:
                    end -= 1
        return track


                
                





        