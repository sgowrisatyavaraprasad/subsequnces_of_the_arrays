class Solution {
    public void rotate(int[][] matrix) {
        int c = matrix.length;
        int[][] arr = new int[c][c];
        int b = matrix.length - 1;
        for(int i = 0; i < c; i++){
            for(int j = 0; j < c; j++){
                arr[i][j] = matrix[i][j];
            }
        }
        for(int i = 0; i < c; i++){
            for(int j = 0; j < c; j++){
                matrix[i][j] = arr[b - j][i];
            }
        }
    }
}