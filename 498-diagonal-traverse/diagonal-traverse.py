from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]: 
            return []
        
        row, col = len(mat), len(mat[0])
        ans = []
        curr_row, curr_col = 0, 0
        up = True  
        
        while len(ans) < row * col:
            ans.append(mat[curr_row][curr_col])
            
            if up: 
                if curr_col == col - 1:  
                    curr_row += 1
                    up = False
                elif curr_row == 0:  
                    curr_col += 1
                    up = False
                else:  
                    curr_row -= 1
                    curr_col += 1
            else:  
                if curr_row == row - 1: 
                    curr_col += 1
                    up = True
                elif curr_col == 0:  
                    curr_row += 1
                    up = True
                else:  
                    curr_row += 1
                    curr_col -= 1
        
        return ans