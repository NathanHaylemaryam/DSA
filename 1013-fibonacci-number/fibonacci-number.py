class Solution:
    def fib(self, n: int) -> int:
        memo = [-1]*(n+1)

        if  n == 0 or n == 1:
            return n

        else:
            if memo[n] == -1:
                memo[n] = self.fib(n-1) + self.fib(n- 2)

        return memo[n]