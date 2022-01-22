class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        sp, ep = 0, len(nums)-1
        while sp<=ep:
            mid = (sp+ep)//2
            if target == nums[mid]:
                return mid
            
            if target < nums[mid]:
                ep = mid - 1
            else:
                sp = mid + 1
                
        return sp
