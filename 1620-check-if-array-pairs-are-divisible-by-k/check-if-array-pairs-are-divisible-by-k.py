class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        for i in range(len(arr)):
            arr[i] = arr[i] % k

        table = Counter(arr)

        print(table)

        if table[0] % 2 == 1:
            return False




        for i in table:
            if i !=0 and table[k-i] != table[i]:
                return False

        return True
        



        


        