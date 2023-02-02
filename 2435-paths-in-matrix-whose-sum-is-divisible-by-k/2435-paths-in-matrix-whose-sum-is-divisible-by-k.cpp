class Solution {
public:
    using ll = long long int;
    vector<vector<vector<ll>>> dp;
    int n, m;
    ll mod = 1e9 + 7;
    
    ll solve(int i, int j, int sum, vector<vector<int>>& grid, int k){
        if(i >= m || j >= n) return 0;
        if(i == m-1 && j == n-1){
            return 0 == ((sum + grid[i][j]) % k);
        }
        if(dp[i][j][sum] != -1) return dp[i][j][sum] % mod;
        ll down = solve(i+1, j, (sum + grid[i][j]) % k, grid, k) % mod;
        ll right = solve(i, j+1, (sum + grid[i][j]) % k, grid, k) % mod;
        return dp[i][j][sum] = (down + right) % mod; 
    }
    
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        m = grid.size();
        n = grid[0].size();
        dp.resize(m, vector<vector<ll>>(n, vector<ll>(k+1, -1)));
        return solve(0, 0, 0, grid, k) % mod;
    }
};