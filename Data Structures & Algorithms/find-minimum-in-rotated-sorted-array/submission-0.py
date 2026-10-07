class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 1
        r = len(nums)-1
        res = nums[0]
        while l <= r:
            m = l + (r-l)//2
            if nums[m] <= res:
                res = nums[m]
                r = m-1
            else:
                l = m+1
        return res

        