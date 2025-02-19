class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Initialize the direction of traversal (1 for upward, -1 for downward)
        Dir = 1  
        
        # Get the dimensions of the matrix
        m = len(mat)    # Number of rows
        n = len(mat[0]) # Number of columns
        
        # Create a result array to store the diagonal traversal
        result = [0] * (m * n)
        print(result)  # Debugging statement to check the initialized result list
        
        # Initialize row, column, and index pointers
        row, col, index = 0, 0, 0
        
        # Traverse until we fill the result array
        while index < m * n:
            # Store the current matrix element in result
            result[index] = mat[row][col]
            index += 1  # Move to the next position in result array
            
            # If moving upwards
            if Dir == 1:
                if col == n - 1:  # If at last column, move down and change direction
                    Dir = -1
                    row += 1
                elif row == 0:  # If at first row, move right and change direction
                    Dir = -1
                    col += 1
                else:  # Otherwise, move diagonally upwards
                    row -= 1
                    col += 1
            
            # If moving downwards
            elif Dir == -1:
                if row == m - 1:  # If at last row, move right and change direction
                    Dir = 1
                    col += 1
                elif col == 0:  # If at first column, move down and change direction
                    Dir = 1
                    row += 1
                else:  # Otherwise, move diagonally downwards
                    row += 1
                    col -= 1
        
        return result  # Return the final diagonal order traversal list

# Time Complexity: O(m * n) - Each element is visited once.
# Space Complexity: O(1) - Output space is not considered in auxiliary space calculation.









        
