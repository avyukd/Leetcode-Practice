class Solution {
public:
    int minKnightMoves(int x, int y) {
        // Symmetry for axes
        x = abs(x); y = abs(y);
        // Symmetry for diagonal
        if (x < y) {
            swap(x, y);
        }
        if (x == 1 && y == 0) {
            return 3;
        }
        if (x == 2 && y == 2) {
            return 4;
        }
        int delta = x - y;
        if (y > delta) {
            return (int) (delta - 2 * floor((float) (delta - y) / 3));
        } else {
            return (int) (delta - 2 * floor((delta - y) / 4));
        }
        
        
        
        /*so the problem with the below is it's too slow. why?
        because i'm using map and set instead of unordered map/unordered set
        unordered set / map can't hash vectors or pairs 
        a potential solution could be turn coordinates into strings, but that's a hassle honestly
        better off doing this in a different language
        
        edit: could make a solution with bitmaps but too lazy rn, get the idea of how to do it
        */
        
        /*
        //using bfs

        
        //map<pair<int, int>, pair<int, int>> parent; 
        //set<pair<int, int>> visited; 
        
        vector<vector<bool>> visited(605, vector<bool>(605)); 
        vector<vector<pair<int, int>>> parents(605, vector<pair<int, int>>(605)); 
        
        /*pair<int, int> start;
        start.first = 0; 
        start.second = 0;
        parent[start] = start; //treating start as a dummy variable*/
        /*
        auto start = make_pair(0, 0);
        parents[0][0] = start;
            
        vector<vector<int>> moves = {
            {2, 1}, {1, 2}, {-1, 2}, {-2, 1}, 
            {-1, -2}, {-2, -1}, {2, -1}, {1, -2}
        };
        
        queue<pair<int, int>> bfs;  
        bfs.push(start); 
        
        while(!bfs.empty()){
            auto top = bfs.front(); bfs.pop();
            if(top.first == x && top.second == y) break; 
            if(!visited[top.first][top.second]){  
                visited[top.first][top.second] = true;
                for(auto &move : moves){
                    pair<int, int> neighbor;
                    neighbor.first = top.first + move[0];
                    neighbor.second = top.second + move[1];
                    bfs.push(neighbor);
                    parents[neighbor.first][neighbor.second] = top; 
                }
            }
        }
        int numMoves = 0;
        auto end_loc = bfs.front(); 
        while(end_loc != start){
            end_loc = parents[end_loc.first][end_loc.second];
            numMoves++;
        }
        return numMoves;
        */
    }
};