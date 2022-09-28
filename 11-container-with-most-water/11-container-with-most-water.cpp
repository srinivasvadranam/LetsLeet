class Solution {
public:
    int maxArea(vector<int>& height) {
        int st=0;
        int n=height.size();
        int e=n-1;
        int ans=0;
        while(st<e)
        {
            ans=max(ans,min(height[st],height[e])*(e-st));
            if(height[st]>=height[e]) e--;
            else st++;
        }
        
        return ans;
    }
};