class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size(), n = heights[0].size();
        
        vector<vector<bool>> pacific(m, vector<bool>(n));
        vector<vector<bool>> atlantic(m, vector<bool>(n));
        
        vector<vector<int>> solution;
        
        vector<vector<int>> pacificStart;
        vector<vector<int>> atlanticStart;
        
        pacificStart.reserve(m + n);
        atlanticStart.reserve(m + n);
        
        for(int j = 0 ; j < n ; j++){
            pacificStart.push_back({0, j});
            atlanticStart.push_back({m - 1, j});
        }
        
        for(int i = 0 ; i < m; i++){
            pacificStart.push_back({i, 0});
            atlanticStart.push_back({i, n - 1});
        }
        
        bfs(heights, atlanticStart, atlantic, m, n);
        bfs(heights, pacificStart, pacific, m, n);
        
        for(int i = 0 ; i < m ; i++){
            for(int j = 0 ; j < n ; j++){
                if(atlantic[i][j] && pacific[i][j])
                    solution.push_back({i, j});
            }
        }
        
        return solution;
    }
    
    void bfs(const vector<vector<int>> & grid, vector<vector<int>> & start, vector<vector<bool>> & sol, int m, int n){
        vector<vector<int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        
        queue<vector<int>> q;
        for(auto & val : start)
            q.push(val);
        
        while(!q.empty()){
            vector<int> nxt = q.front(); q.pop();
                        
            int i = nxt[0];
            int j = nxt[1];
            
            if(!sol[i][j]){
                sol[i][j] = 1;
                for(auto & dir : dirs){
                    int ni = i + dir[0], nj = j + dir[1];
                    if(ni >= 0 && nj >= 0 && ni < m && nj < n 
                        && grid[ni][nj] >= grid[i][j]){
                        q.push({ni, nj});
                    }
                }
            }
        }
    }
};