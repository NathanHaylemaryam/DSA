class Solution:
    def countPrimes(self, n: int) -> int:

        if n < 3:
            return 0

        is_prime = [True] * (n // 2)

        for i in range(1, int(n**0.5) // 2 + 1):
            if is_prime[i]:
                p = 2 * i + 1
                for multiple in range(p * p, n, 2 * p):
                    is_prime[multiple // 2] = False
        return 1 + sum(is_prime[1:]) 
