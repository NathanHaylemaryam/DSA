class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowel , con  =0 , 0
        vow = {'a', 'e', 'i', 'o','u'}
        for i in word:
            if not i.isalnum():
                return False
            
            if i.isalpha():
                if i.lower() in vow:
                    vowel += 2
                else:
                    con += 1
        return vowel > 0 and con > 0