class Solution:
    def isPalindrome(self, s: int) -> bool:
        if s == 0:
            return True
        if s < 0:
            return False

        arr1 = str(s)
        if arr1[-1] == '0':
            return False
        
        arr2 = arr1[::-1]
        print(arr1, arr2)
        

        for i in range(len(arr1)):
            if arr1[i] == arr2[i]:
                continue
            else:
                return False
        return True
        