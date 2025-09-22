class Solution:
 
    def climbStairs(self, n: int) -> int:
        memo  = [-1]*(n + 1)

        def solve(n):
            if n == 1 or n== 2:
                return n

            if memo[n] == -1:
                memo[n] = solve(n - 1) + solve(n - 2)

            return memo[n]

        return solve(n)

        

        

        