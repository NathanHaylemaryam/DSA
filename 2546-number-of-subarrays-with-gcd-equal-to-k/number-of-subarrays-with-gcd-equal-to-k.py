class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0
        
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = math.gcd(g, nums[j])
                if g == k:
                    cnt += 1
                elif g < k:
                    
                    break
        return cnt
