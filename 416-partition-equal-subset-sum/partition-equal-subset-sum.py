class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = defaultdict(bool)
        if sum(nums) % 2 == 1: return False

        target = sum(nums) // 2
        

        def dp(curr , i):
            if curr == target:
                return True
            elif curr > target:
                return False

            else:
                if i < len(nums):
                    if (curr , i) in memo:
                        return memo[(curr, i)]
                    else:
                        memo[(curr,i)] =  dp(curr + nums[i] ,  i+ 1) or dp(curr , i + 1)
                        return memo[(curr, i)]
                else:
                    return False
        return dp(0 , 0)

            

    
        