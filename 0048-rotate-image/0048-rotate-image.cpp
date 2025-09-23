class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int a = 0 , b = matrix.size() - 1;
        int c = matrix.size();
        vector<vector<int>>vec(c , vector<int>(c , 0));
        for(int i = 0; i < matrix.size(); i++){
            for(int j = 0; j < matrix[i].size(); j++){
                vec[i][j] = matrix[i][j];
            }
        }
        for(int i = 0; i < vec.size(); i++){
            for(int j = 0; j < vec[i].size(); j++){
                matrix[i][j] = vec[b - j][i];
            }
            cout << endl;
        }
        
    }
};