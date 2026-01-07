class Solution {
    public int maxSum(int[][] grid) {
        int[] arr = new int[grid.length * grid[0].length];
        int c = 0;
        for(int i = 0; i < grid.length; i++){
            int sum = 0;
            for(int j = 0; j < grid[i].length; j++){
                if(i + 2 < grid.length && j + 2 < grid[i].length){
                    int a = (grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[i + 1][j + 1]);
                    a += (grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]);
                    sum = a;
                }
                arr[c++] = sum;
                
            }
        }
        int max = Arrays.stream(arr).max().getAsInt();
        return max;
    }
}