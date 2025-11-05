class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        
        def helper(index, current_sum):
            if index == n:
                return 1 if current_sum == target else 0
            
            if (index, current_sum) not in memo:
                result = 0
                result += helper(index + 1, current_sum + nums[index])
                result += helper(index + 1, current_sum - nums[index])
                memo[(index, current_sum)] = result
            
            return memo[(index, current_sum)]
        
        return helper(0, 0)