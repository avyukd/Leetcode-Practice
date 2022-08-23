class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        
        int i = m - 1, j = 0;
        
        while(i > 0){
            diagSortHelper(mat, i, j, m, n);
            --i;
        }
        
        i = 0, j = 0;
        while(j < n){
            diagSortHelper(mat, i, j, m, n);
            ++j;
        }
        
        return mat;
    }
    
    void diagSortHelper(vector<vector<int>>& mat, int i, int j, int m, int n){
        int si = i, sj = j;
        vector<int> diag;
        while(si < m and sj < n){
            diag.push_back(mat[si][sj]);
            ++si; ++sj;
        }
        sort(diag.begin(), diag.end());
        si = i, sj = j; int idx = 0;
        while(si < m and sj < n){
            mat[si][sj] = diag[idx];
            ++idx; ++si; ++sj;
        }
    }
};