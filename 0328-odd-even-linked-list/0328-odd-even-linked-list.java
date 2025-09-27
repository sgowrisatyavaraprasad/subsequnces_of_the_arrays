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
//  class Node{
//     int val;
//     Node next;
//     Node(int val){
//         this.val = val;
//         next = null;
//     }
//  }
 class Linked{
    public static ListNode insert(int val , ListNode res){
        ListNode newnode = new ListNode(val);
        if(res == null){
            res = newnode;
            return res;
        }
        else{
            ListNode temp = res;
            while(temp.next != null){
                temp = temp.next;
            }
            temp.next = newnode;
        }
        return res;
    }
 }
class Solution {
    public ListNode oddEvenList(ListNode head) {
        Linked obj = new Linked();
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(ListNode temp = head; temp != null; temp = temp.next){
            list.add(temp.val);
        }
        ArrayList<Integer> odd = new ArrayList<Integer>();
        ArrayList<Integer> even = new ArrayList<Integer>();
        ListNode res = null;
        for(int i = 0; i < list.size(); i++){
            if(i % 2 != 0){
                odd.add(list.get(i));
            }
            else{
                even.add(list.get(i));
            }
        }
        ArrayList<Integer> list1 = new ArrayList<Integer>();
        for(int i = 0; i < even.size(); i++){
            list1.add(even.get(i));
        }
        for(int i = 0; i < odd.size(); i++){
            list1.add(odd.get(i));
        }
        for(int i = 0; i  < list1.size(); i++){
            res = obj.insert(list1.get(i) , res);
        }
        return res;
    }
}