class Solution {
    public int divisorSubstrings(int num, int k) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        int num1 = num;
        int cout = 0;
        while(num != 0){
            int a = num % 10;
            list.add(a);
            num = num / 10;
        }
        int[] arr = new int[list.size()];
        int c = 0;
        for(int i = list.size() - 1; i >= 0; i--){
            arr[c++] = list.get(i);
        }
        int l = 0 , r = k - 1;
        while(r < c){
            int sum = 0;
            for(int i = l; i <= r; i++){
                sum = (sum * 10) + arr[i];
            }
            if(sum != 0 && num1 % sum == 0){
                cout++;
            }
            l++;
            r++;
        }
        return cout;
    }
}