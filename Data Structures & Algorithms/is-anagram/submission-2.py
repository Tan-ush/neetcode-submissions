class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2={}
        for i in s:
            if dict1.get(i) == None:
                dict1[i] = 1
            else:
                dict1[i] += 1
        
        for b in t:
            if dict2.get(b) == None:
                dict2[b] = 1
            else:
                dict2[b] += 1
        if dict1 == dict2:
            return True
        return False