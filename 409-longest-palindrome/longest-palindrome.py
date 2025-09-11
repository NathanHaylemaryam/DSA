class Solution:
    def longestPalindrome(self, s: str) -> int:
        table = defaultdict(int)
        cnt = 0

        for ch in s:
            table[ch] += 1

        odd_found = False

        for val in table.values():
            if val % 2 == 0:
                cnt += val
            else:
                cnt += val - 1
                odd_found = True

        
        if odd_found:
            cnt += 1

        return cnt
