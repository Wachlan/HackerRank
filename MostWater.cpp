
// You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

// Find two lines that together with the x-axis form a container, such that the container contains the most water.

// Return the maximum amount of water a container can store.

class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxarea = 0;
        int left = 0;
        int right = height.size() - 1;
        
        while (right >= left)
        {
            int width = right - left;
            int area = min(height[left],height[right]) * width;
            if (area > maxarea)
            {
                maxarea = area;
            }
            
            if (height[right] <= height[left])
            {
                right--;
            } else
            {
                left++;
            }
            
        }
        
        
        
        
        
        return maxarea;
    }
};