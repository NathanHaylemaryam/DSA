class Solution:
    def __init__ (self):
        self.memo = defaultdict(int)
    def climbStairs(self, n: int) -> int:

        if n == 1 or n == 2:
            return n

        else:
            if n not in self.memo:
                self.memo[n]  = self.climbStairs(n - 1) + self.climbStairs(n-2)

        return self.memo[n]

        

        