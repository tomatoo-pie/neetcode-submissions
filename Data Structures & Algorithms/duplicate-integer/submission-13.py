from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        temp = []
        if nums == temp:
            return False
        else:
            for i in range(len(nums)):
                seen.add(nums[i])
                if len(seen) == len(nums):
                    return False
        return True
        


        