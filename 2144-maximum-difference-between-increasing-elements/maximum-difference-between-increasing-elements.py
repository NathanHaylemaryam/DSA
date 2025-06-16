class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        for j in range(len(nums)):
            for i in range(j,len(nums)):
                if nums[j] < nums[i]:
                    ans = max(ans , nums[i] - nums[j])
        return ans