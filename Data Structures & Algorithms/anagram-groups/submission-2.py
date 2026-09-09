class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dict = defaultdict(list)
        for s in strs:
            new = ''.join(sorted(s))
            dict[new].append(s)
        return list(dict.values())




                

