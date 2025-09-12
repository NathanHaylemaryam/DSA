class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table = Counter( magazine)

        for i in range(len(ransomNote)):
            if table[ransomNote[i]] > 0:
                table[ransomNote[i]] -= 1
            else:
                return False

        return True

        