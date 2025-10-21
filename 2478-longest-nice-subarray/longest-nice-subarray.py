class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        mask = 0
        left = 0
        res = 0

        for right in range(len(nums)):
            while mask & nums[right]:
                mask ^= nums[left]  
                left += 1
            mask |= nums[right] 
            res = max(res, right - left + 1)
        
            

        return res