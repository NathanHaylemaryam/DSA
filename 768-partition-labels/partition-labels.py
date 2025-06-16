class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        table = defaultdict(int)
        for i in range(len(s)):
            table[s[i]]  = i
        print(table) 
        ans  = []
        size = 0
        end = table[s[0]]
        for i in range(len(s)):
            size += 1

            end = max(end, table[s[i]])

            if i == end:
                ans.append(size)
                size = 0 
            
            
                

            
            
        return ans
                
