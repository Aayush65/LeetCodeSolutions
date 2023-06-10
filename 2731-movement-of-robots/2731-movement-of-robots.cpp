class Solution {
public:
    int MOD = 1000000007;
    int sumDistance(vector<int>& nums, string s, int d) {
        for(int i = 0; i < nums.size(); i++){
            if(s[i] == 'R') nums[i] += d;
            else nums[i] -= d;
        }
        long long ans = 0;
        long long pref = 0;
        sort(nums.begin(), nums.end());
        long long n = s.length()-1;
        for(long long i = 0; i < nums.size(); i++){
            ans += i * (long long) nums[i] - pref;
            ans %= MOD;
            pref += nums[i];
        }
        return ans;
    }
};