class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
            burte-force:
            double for-loop scan for zeros
            double for-loop for those x, y having zeros --> No, save space complexity
            *but we cannot directly update on-the-fly, since later elements would be polluted...

            => 
        '''
        # double double for-loop version
        # time complexity O(m*n)
        # space cimplexity O(m*n) worst case
        zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zeros.append([i,j])
        
        for zero in zeros:
            for j in range(len(matrix[0])):
                matrix[zero[0]][j] = 0
            for i in range(len(matrix)):
                matrix[i][zero[1]] = 0