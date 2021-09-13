class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int N = text1.length(); 
        int M = text2.length(); 
        vector<vector<int>> memo(N+1, vector<int>(M+1, 0)); 
        for(int i = 1 ; i <= N; i++){
            for(int j = 1 ; j <= M; j++){
                if(text1[i-1] == text2[j-1]){
                    memo[i][j] = memo[i-1][j-1]+1; 
                }else{
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1]);
                }
            }
        }
        return memo[N][M];
    }
};