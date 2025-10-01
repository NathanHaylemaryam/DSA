class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

   

        dp = [0]*len(nums)

        for i in range(len(nums)):
            x = nums[i]
            temp = 1
            for j in range(i):

                if x > nums[j]:

                    dp[i] = max(dp[j], dp[i]) 
            dp[i] += 1

            

        
        return max(dp)

        