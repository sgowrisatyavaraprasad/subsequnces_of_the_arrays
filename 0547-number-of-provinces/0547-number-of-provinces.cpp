class Solution {
public:
    void dfs(int node , vector<vector<int>>& adj , vector<int>& vis){
        vis[node] = 1;
        for(auto ele : adj[node]){
            if(vis[ele] == 0){
                vis[ele] = 1;
                dfs(ele , adj , vis);
            }
        }
    }
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<vector<int>> adj;
        adj.resize(n);
        for(int i = 0; i < isConnected.size(); i++){
            for(int j = 0; j < isConnected.size(); j++){
                if(isConnected[i][j] == 1 && i != j){
                    adj[i].push_back(j);
                    adj[j].push_back(i);
                }
            }
        }
        int c = 0;
        vector<int> vis(n , 0);
        for(int i = 0; i < adj.size(); i++){
            if(!vis[i]){
                c += 1;
                dfs(i , adj , vis);
            }
        }
        return c;
    }
};