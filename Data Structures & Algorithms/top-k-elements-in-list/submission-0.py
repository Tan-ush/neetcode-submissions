class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        sort = n

        arr=[]
        for a, b in d.items():
            arr.append([b, a])
        arr.sort()

        final = []
        while len(final) < k:
            final.append(arr.pop()[1])
        return final