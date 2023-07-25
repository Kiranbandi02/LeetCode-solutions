#include <algorithm>
class Solution {
public:
    int maximizeSum(vector<int>& nums, int k) {
        int n=nums.size();
        sort(nums.begin(),nums.end());
        long long int a=nums[n-1];
        int i=0;
        while(k>0){
            i=i+a;
            a++;
            k--;
        }
        return i;
    }
};