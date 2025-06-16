class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans =  []
        p1 , p2  = 0 , 0 
        n ,m  =  len(firstList) , len(secondList)
        
        while p1 < n and p2 < m:
            temp1 , temp2 = [firstList[p1]] , [secondList[p2]]
            a ,b = max(temp1[0][0], temp2[0][0]) , min(temp1[0][1], temp2[0][1])
            if a <= b:
                ans.append([a, b])
            if temp2[0][1] == temp1[0][1]:
                p1 += 1
                p2 += 1
            elif temp2[0][1] > temp1[0][1]:
                p1 += 1
            else:
                p2 += 1
        return ans
        