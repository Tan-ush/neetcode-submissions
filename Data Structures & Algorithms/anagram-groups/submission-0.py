class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for s in strs:
            alpha = [0] * 26
            for i in s:
                alpha[ord(i) - ord('a')] += 1
            dict[tuple(alpha)].append(s)
        return list(dict.values())



                

