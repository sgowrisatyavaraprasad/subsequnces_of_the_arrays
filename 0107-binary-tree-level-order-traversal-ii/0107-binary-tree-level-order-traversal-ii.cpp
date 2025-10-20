/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        if(root == nullptr){
            vector<vector<int>>A;
            return A;
        }
        queue<TreeNode*> q;
        q.push(root);
        vector<vector<int>>v;
        while(!q.empty()){
            int s = q.size();
            vector<int>level;
            for(int i = 0; i < s; i++){
                TreeNode *node = q.front();
                if(node != nullptr){
                    level.push_back(node->val);
                }
                q.pop();
                if(node != nullptr){
                    if(node->left != nullptr){
                        q.push(node->left);
                    }
                    if(node->right != nullptr){
                        q.push(node->right);
                    }
                }
            }
            v.push_back(level);
        }
        reverse(v.begin() , v.end());
        return v;
    }
};