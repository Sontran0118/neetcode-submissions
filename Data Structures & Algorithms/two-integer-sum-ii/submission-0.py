class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1
        while l < r:
            sumn = numbers[l] + numbers[r]
            if sumn == target:
                return [l+1,r+1]
            if sumn > target:
                r -= 1
            if sumn < target:
                l += 1
        return []
                 

             
        
        