class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapp = {}

        for i in range(len(nums)):
            mapp[nums[i]] = mapp.get(nums[i], 0) + 1

        for i in range(len(nums)):
            if mapp[nums[i]] > 1:
                return True

        return False
        