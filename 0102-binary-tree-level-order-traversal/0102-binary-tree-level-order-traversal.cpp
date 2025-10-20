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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(root == nullptr){
            vector<vector<int>>A;
            return A;
        }
        vector<vector<int>>v;
        queue<TreeNode*>q;
        q.push(root);
        while(!q.empty()){
            TreeNode *node = q.front();
            int s = q.size();
            vector<int>level;
            for(int i = 0; i < s; i++){
                TreeNode *node1 = q.front();
                if(node1 != nullptr)
                    level.push_back(node1->val);
                q.pop();
                if(node1 != nullptr){
                    if(node1->left != nullptr){
                        q.push(node1->left);
                    }
                    if(node1->right != nullptr){
                        q.push(node1->right);
                    }
                }
            }
            v.push_back(level);
        }
        return v;
    }
};