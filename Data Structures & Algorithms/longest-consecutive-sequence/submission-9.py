class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        if(len(nums) == 1):
            return 1
        nums.sort()
        best = 1
        current = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                current += 1
            else:
                best = max(best, current)
                current = 1
            
        best = max(current,best)
        return best
        