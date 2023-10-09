class Solution {
public:
    
    
    bool canPartition(vector<int>& arr) {
        int sum=accumulate(arr.begin(),arr.end(),0);
        if(sum%2!=0){
            return false;
        }
        int n=arr.size();
        //vector<vector<int>> dp(n,vector<int>(sum/2+1,-1));
        int k=sum/2;
        vector<bool>prev(k+1,false),cur(k+1,false);
        prev[0]=true;
        cur[0]=true;
        for(int i=1;i<n;i++ ){
            //vector<bool>cur(k+1,false);
            //r[0]=true;
            for(int j=1;j<=k;j++){
                bool ntake=prev[j];
                bool take=false;
                if(arr[i]<=j){
                    take=prev[j-arr[i]];
                }
                cur[j]=take||ntake;
                
            }
            prev=cur;
            
            
        }
        return prev[k];    
    }
};