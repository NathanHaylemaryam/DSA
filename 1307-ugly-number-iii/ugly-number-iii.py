

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def count_divisible(mid, a, b, c):
            ab = math.lcm(a, b)
            ac = math.lcm(a, c)
            bc = math.lcm(b, c)
            abc = math.lcm(a, b, c)
            return (mid // a + mid // b + mid // c
                    - mid // ab - mid // ac - mid // bc
                    + mid // abc)

        l, r = 1, 10**18
        while l < r:
            mid = (l + r) // 2
            if count_divisible(mid, a, b, c) >= n:
                r = mid
            else:
                l = mid + 1
        return l
