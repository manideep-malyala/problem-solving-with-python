class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        model = {}
        for i in range(len(nums)):
            if target-nums[i] in model:
                return [model[target-nums[i]], i]
            else:
                model[nums[i]]=i
