class Solution:
    def rob(self, nums: List[int]) -> int:

      
        if len(nums) <= 2:
            return max(nums)
        dp  = [0,nums[0]]


        for i in range(1, len(nums)):
            dp.append(max(dp[i-1]+nums[i] , dp[i]))
        print(dp)

        return dp[-1]





        