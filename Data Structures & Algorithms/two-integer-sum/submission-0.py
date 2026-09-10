class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {}

        for i in range(len(nums)):
            if nums[i] not in num_dic :
                num_dic[target-nums[i]] = i
            else:
                return [num_dic[nums[i]], i]
        
        return []