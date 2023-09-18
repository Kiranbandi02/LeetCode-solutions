class Solution {
public:
    bool canJump(vector<int>& nums) {
        int r=0;
        int n=nums.size();
        for(int i=0;i<n;i++){
            if(r<i){
                return false;
            }
            r=max(r,i+nums[i]);
        }
        return true;
        
        
        

        
    }
};