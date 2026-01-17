/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[][] spiralMatrix(int m, int n, ListNode head) {
        int[][] arr = new int[m][n];
        int c = 0;
        int l = 0 , r = arr[0].length - 1;
        int t = 0 , b = arr.length - 1;
        while(l <= r && t <= b){
            for(int j = l; j <= r; j++){
                if(head != null){
                    arr[t][j] = head.val;
                    head = head.next;
                    c += 1;
                }
                else{
                    arr[t][j] = -1;
                }
            }
            t += 1;
            for(int j = t; j <= b; j++){
                if(head != null){
                    arr[j][r] = head.val;
                    head = head.next;
                    c += 1;
                }
                else{
                    arr[j][r] = -1;
                }
            }
            r -= 1;
            if(t <= b){
                for(int j = r; j >= l; j--){
                    if(head != null){
                        arr[b][j] = head.val;
                        head = head.next;
                        c += 1;
                    }
                    else{
                        arr[b][j] = -1;
                    }
                }
                b -= 1;
            }
            if(l <= r){
                for(int j = b; j >= t; j--){
                    if(head != null){
                        arr[j][l] = head.val;
                        head = head.next;
                        c += 1;
                    }
                    else{
                        arr[j][l] = -1;
                    }
                }
                l += 1;
            }
        }
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j ++){
                System.out.print(arr[i][j] +  " ");
            }
            System.out.println();
        }
        return arr;
    }
}