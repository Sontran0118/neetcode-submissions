class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for m in range(len(nums) - 2):

            # Skip duplicate fixed values
            if m > 0 and nums[m] == nums[m - 1]:
                continue

            l = m + 1
            r = len(nums) - 1

            while l < r:

                sum3 = nums[m] + nums[l] + nums[r]

                if sum3 == 0:
                    res.append([nums[m], nums[l], nums[r]])

                    # Skip duplicates
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1

                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

                elif sum3 < 0:
                    l += 1

                else:
                    r -= 1

        return res