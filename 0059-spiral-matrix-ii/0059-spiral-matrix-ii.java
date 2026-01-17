class Solution {
    public int[][] generateMatrix(int n) {
        int[][] arr = new int[n][n];
        int l = 0 , r = n - 1;
        int t = 0 , b = n - 1;
        int c = 1;
        while(l <= r && t <= b){
            for(int i = l; i <= r; i++){
                arr[t][i] = c;
                c += 1;
            }
            t += 1;
            for(int i = t; i <= b; i++){
                arr[i][r] = c;
                c += 1;
            }
            r -= 1;
            if(t <= b){
                for(int i = r; i >= l; i--){
                    arr[b][i] = c;
                    c += 1;
                }
                b -= 1;
            }
            if(l <= r){
                for(int i = b; i >= t; i--){
                    arr[i][l] = c;
                    c += 1;
                }
                l += 1;
            }
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println(l + " "  + r + " "  + t  + " " +  b);
        return arr;
    }
}