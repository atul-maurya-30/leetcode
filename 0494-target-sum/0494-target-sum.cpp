class Solution {
public:
    int solve(vector<int>&nums,int i,int s,int target){
        if (i==nums.size()){
            return s==target ? 1 : 0;
        }
        return solve(nums,i+1,s+nums[i],target)+solve(nums,i+1,s-nums[i],target);
    }
    int findTargetSumWays(vector<int>& nums, int target) {
        return solve(nums,0,0,target);
    }
};