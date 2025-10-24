class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        
        while n != 1:
            if n in seen:
                return False  
            seen.add(n)
            
            ans = 0
            while n > 0:
                ans += (n % 10) ** 2
                n //= 10
            n = ans
        
        return True
        