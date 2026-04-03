# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)) :
#             for j in range(i+1, len(nums)) :
#                 if nums[i] == nums[j] :
#                     return True
#                 else :
#                     continue
#         return False

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = set()
        for i in range(len(nums)) :
            if nums[i] in store :
                return True
            else :
                store.add(nums[i])
        return False
            



