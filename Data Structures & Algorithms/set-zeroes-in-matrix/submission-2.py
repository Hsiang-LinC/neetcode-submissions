class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
            burte-force:
            double for-loop scan for zeros
            double for-loop for those x, y having zeros --> No, save space complexity
            *but we cannot directly update on-the-fly, since later elements would be polluted...
            # alterative: use 2 array to store 0-infos, one for col, one for row
            # alterative: store in-place to avoid extra storage. Store on the col and row of a zero

            => 
        '''
        # double double for-loop version
        # time complexity O(m*n)
        # space cimplexity O(m*n) worst case
        zeros = [0 for _ in range(len(matrix))], [0 for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zeros[0][i] = 1
                    zeros[1][j] = 1
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if zeros[0][i] or zeros[1][j]:
                    matrix[i][j] = 0
        
        
