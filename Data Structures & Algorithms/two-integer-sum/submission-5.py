class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}

        for i in range(len(nums)):
            mapp[nums[i]] = i

        for i in range(len(nums)):
            diffe = target - nums[i]
            if diffe in mapp and mapp[diffe] != i:
                return sorted([mapp[diffe],i])
        
        return []
 
        