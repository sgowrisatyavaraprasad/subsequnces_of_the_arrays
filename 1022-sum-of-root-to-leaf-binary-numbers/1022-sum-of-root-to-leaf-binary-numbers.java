/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public static void function(TreeNode temp , String res ,List<Integer> list , int len , int sum , int c){
            int sum1 = 0;
            if(temp != null){
                res += temp.val;
                if(temp.left == null && temp.right == null){
                    int a = Integer.parseInt(res , 2);
                    list.add(a);
                }
                
                function(temp.left , res , list , len , sum , c);
                
                function(temp.right , res , list , len , sum , c);
                // System.out.println(res);
            }
    }
    public int sumRootToLeaf(TreeNode root) {
        TreeNode temp = root;
        String res = "";
        List<Integer> list = new ArrayList<Integer>();
        int sum = 0;
        int c= 0;
        int len = 0;
        // System.out.println(len);
        function(root , res , list , len , sum , c);
        for(int i : list){
            sum += i;
        }
        System.out.println(sum);
        return sum;
    }
}