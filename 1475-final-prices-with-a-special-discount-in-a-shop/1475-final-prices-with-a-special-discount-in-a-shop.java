class Solution {
    public int[] finalPrices(int[] prices) {
        int[] arr = new int[prices.length];
        int c = 0;
        for(int i = 0; i < prices.length; i++){
            int count = 0;
            for(int j = i; j < prices.length; j++){
                if(j > i && prices[j] <= prices[i]){
                    arr[c++] = prices[i] - prices[j];
                    count += 1;
                    break;
                }
            }
            if(count == 0){
                arr[c++] = prices[i];
            }
            continue;
        }
        for(int i = 0; i < c; i++){
            System.out.print(arr[i] + " ");
        }
        return arr;
    }
}