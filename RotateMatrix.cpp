// You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

class Solution {
public:
    void rotate(vector<vector<int>>& matrix)
    {
        transpose(matrix);
        reverse(matrix);
    }
    
    void transpose(vector<vector<int>>& matrix)
    {
        int i = matrix.size();
        for (int row = 0; row < i; row++)
        {
            for (int col = row + 1; col < i; col++)
            {
                int temp = matrix[col][row];
                matrix[col][row] = matrix[row][col];
                matrix[row][col] = temp;
            }
        }
        
        return;
    }
    
    void reverse(vector<vector<int>>& matrix)
    {
        int i = matrix.size();
        
        for (int row = 0; row < i; row++)
        {
            for (int col = 0; col < i/2; col++)
            {
                int temp = matrix[row][col];
                matrix[row][col] = matrix[row][i - col - 1];
                matrix[row][i - col - 1] = temp;
            }
        }
        
        return;
    }
};