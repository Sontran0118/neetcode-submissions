class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dic = {}
        for i in range(len(nums)):

            if nums[i] not in nums_dic:
                nums_dic[nums[i]] = True
            else:
                return True
        return False
            
            
        