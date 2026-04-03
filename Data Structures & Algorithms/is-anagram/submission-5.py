# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if sorted(s) == sorted(t) :
#             return True
#         else :
#             return False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_1 = {}
        hashmap_2 = {}
        for i in range(min(len(s), len(t))) :
            hashmap_1[s[i]] = s.count(s[i])
            hashmap_2[t[i]] = t.count(t[i])
        if len(s) == len(t) and hashmap_1 == hashmap_2 :
            return True
        return False








