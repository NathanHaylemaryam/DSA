class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:

            return max(nums)
        def house_robber_one(nums):
            a , b = 0 , nums[0]

            for i in range(1 , len(nums)):

                temp = b

                b = max(nums[i] + a, b)

                a = temp

            return b

        n = len(nums)

        print(nums[:n-1])
        print(nums[1:])

        return max(house_robber_one(nums[:n-1]) , house_robber_one(nums[1:]))


       

