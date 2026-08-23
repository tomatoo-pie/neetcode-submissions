class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapp= {}

        for i in range(len(nums)):
            mapp[nums[i]] = mapp.get(nums[i], 0) + 1

        if len(mapp) != len(nums):
            return True

        return False
        