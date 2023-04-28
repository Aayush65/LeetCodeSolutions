class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n=matrix.size();
        int m=matrix[0].size();

        for(int i=0;i<n;i++){
            int size=matrix[i].size();
            int low=0;
            int high=size-1;
            while(low<=high){
                int mid=(low+high)/2;
                if(matrix[i][mid]==target){
                    return true;
                }
                else if(matrix[i][mid]>target){
                    high=mid-1;
                }
                else{
                    low=mid+1;
                }
            }
        }
        return false;
    }
};