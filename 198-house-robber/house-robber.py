class Solution:
    def rob(self, nums: List[int]) -> int:
        

        if len(nums) <= 2:
            return max(nums)

        a , b  = 0 , nums[0]

        for i in range(1,len(nums)):

            temp = b

            b = max(a + nums[i] , b)

            a =  temp
            

        return b


        