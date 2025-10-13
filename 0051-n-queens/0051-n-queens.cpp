class Solution {
public:
    bool isValid(int i , int j , vector<string>&A , int n){
        int ti = i , tj = j;
        while(ti >= 0){
            if(A[ti][tj] == 'Q'){
                return false;
            }
            ti--;
        }
        ti = i , tj = j;
        while(ti >= 0 && tj >= 0){
            if(A[ti][tj] == 'Q'){
                return false;
            }
            ti--;
            tj--;
        }
        ti = i , tj = j;
        while(ti >=0 && tj < n){
            if(A[ti][tj] == 'Q'){
                return false;
            }
            ti--;
            tj++;
        }
        return true;
    }
    void slove(int row , int n , vector<string>&A , vector<vector<string>>&ds){
        if(row == n){
            ds.push_back(A);
            return;
        }
        for(int j = 0; j < n; j++){
            if(isValid(row , j , A , n)){
                A[row][j] = 'Q';
                slove(row + 1 , n , A , ds);
                A[row][j] = '.';
            }
        }
    }
    vector<vector<string>> solveNQueens(int n) {
        vector<string>A;
        vector<vector<string>>ans;
        for(int i = 0; i < n; i++){
            string s;
            for(int j = 0; j < n; j++){
                s += '.';
            }
           A.push_back(s);
        }
        slove(0 , n , A , ans);
        return ans;
    }
};