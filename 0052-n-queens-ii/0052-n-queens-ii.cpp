class Solution {
public:
    bool isValid(int i , int j , int n , vector<string>&A){
        int ti = i , tj = j;
        while(ti >= 0 && tj >= 0){
            if(A[ti][tj] == 'Q'){
                return false;
            }
            ti--;
            tj--;
        }
        ti = i , tj = j;
        while(ti >= 0){
            if(A[ti][tj] == 'Q'){
                return false;
            }
            ti--;
        }
        ti = i , tj = j;
        while(ti >= 0 && tj < n){
            if(A[ti][tj] == 'Q'){
                return false;
            }
            ti--;
            tj++;
        }
        return true;
    }
    void slove(int r , int n , vector<vector<string>>&ans , vector<string>&A){
        if(r == n){
            ans.push_back(A);
            return;
        }
        for(int i = 0; i < n; i++){
            if(isValid(r , i , n , A)){
                A[r][i] = 'Q';
                slove(r + 1 , n , ans , A);
                A[r][i] = '.';
            }
        }
    }
    int totalNQueens(int n) {
        vector<vector<string>>ans;
        vector<string>A;
        for(int i = 0; i < n; i++){
            string s;
            for(int j = 0; j < n; j++){
                s += '.';
            }
            A.push_back(s);
        }
        slove(0 , n , ans , A);
        // cout << ans.size() << endl;
        // for(int i = 0; i < ans.size(); i++){
        //     cout << ans[i] << " ";
        // }
        return ans.size();
    }
};