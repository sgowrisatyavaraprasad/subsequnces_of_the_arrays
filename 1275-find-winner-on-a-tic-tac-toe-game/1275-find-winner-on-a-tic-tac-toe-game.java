class Solution {
    public String tictactoe(int[][] moves) {
        int a = 0;
        char[][] arr = new char[3][3];
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                arr[i][j] = ' ';
            }
        }
        for(int i = 0; i < moves.length; i += 1){
            if(i % 2 == 0)
                arr[moves[i][0]][moves[i][1]] = 'x';
            if(i % 2 != 0)
                arr[moves[i][0]][moves[i][1]] = 'o';
        }
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
        int c = 0;
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                if(arr[i][j] == ' '){
                    c += 1;
                }
            }
        }
        for(int i = 0; i < 3; i++){
            int xc = 0 , oc = 0;
            for(int j = 0; j < 3; j++){
                if(arr[i][j] == 'x'){
                    xc += 1;
                }
                if(arr[i][j] == 'o'){
                    oc += 1;
                }
            }
            if(xc == 3){
                return "A";
            }
            if(oc == 3){
                return "B";
            }
        }
        while(a < 3){
            int xc = 0 , oc = 0;
            for(int i = 0; i < 3; i++){
                if(arr[i][a] == 'x'){
                    xc += 1;
                }
                if(arr[i][a] == 'o'){
                    oc += 1;
                }
            }
            if(xc == 3){
                return "A";
            }
            if(oc == 3){
                return "B";
            }
            a += 1;
        }
        if((arr[0][0] == 'x' && arr[1][1] == 'x' && arr[2][2] == 'x') || (arr[2][0] == 'x' && arr[1][1] == 'x' && arr[0][2] == 'x')){
            return "A";
        }
        if((arr[0][0] == 'o' && arr[1][1] == 'o' && arr[2][2] == 'o') || (arr[2][0] == 'o' && arr[1][1] == 'o' && arr[0][2] == 'o')){
            return "B";
        }
        if(c == 0){
            return "Draw";
        }
        return "Pending";
    }
}