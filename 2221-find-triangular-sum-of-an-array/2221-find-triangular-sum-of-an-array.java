class Solution {
    public static int re(int[] nums , int n){
        int[] arr = new int[n];
        int c = 0;
        if(n == 1){
            return nums[0];
        }
        for(int i = 1; i < n; i++){
            if(nums[i - 1] + nums[i] >= 10){
                int a = nums[i - 1] + nums[i];
                arr[c++] = a % 10;
            }
            else{
                arr[c++] = nums[i - 1] + nums[i];
            }
        }
        return re(arr , c);
    }
    public int triangularSum(int[] nums) {
        int res = 0;
        if(nums.length == 1){
            return nums[0];
        }
        else{
            res = re(nums , nums.length);
            System.out.println(res);
        }
        if(res > 10){
            return res % 10;
        }
        return res;
    }
}