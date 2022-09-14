// Given an unsorted integer array nums, return the smallest missing positive integer.


class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        vector arr(n,0);
        
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] <= n && nums[i] > 0)
            {
                arr[nums[i]-1] = 1;
            }
            
        }
        
        for (int i = 0; i < arr.size(); i++)
        {
            if (arr[i] == 0)
            {
                return i+1;
            }
            
        }
        
        return n+1;
    }
};


