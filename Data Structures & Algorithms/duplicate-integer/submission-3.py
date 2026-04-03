class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = {}
        for i in range(len(nums)) :
            if nums[i] in store :
                return True
            else :
                store[nums[i]] = i
        return False
            



