# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)) :
#             for j in range(len(nums)) :
#                 if i != j and nums[i] + nums[j] == target :
#                     return [i,j]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)) :
            difference = target - nums[i]
            if difference in seen :
                return [seen[difference], i]
            else :
                seen[nums[i]] = i



                



