class Solution {
    public int trailingZeroes(int n) {
        int c=0;
        for(int i=5;i<=n;i=i*5){
            c+=n/i;
            
        }
        return c;
    }
}