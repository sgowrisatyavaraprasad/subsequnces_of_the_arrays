class Solution {
    public String removeOuterParentheses(String s) {
        Stack<Character> st = new Stack<>();
        String res = "";
        for(int i = 0; i < s.length(); i++){
            st.push(s.charAt(i));
            int ob = 0;
            int cb = 0;
            if(!st.isEmpty()){
                for(int j = 0; j < st.size(); j++){
                    if(st.get(j) == ')'){
                        cb += 1;
                    }
                    else if(st.get(j) == '('){
                        ob += 1;
                    }
                    else{
                        continue;
                    }
                }
            }
            if(ob == cb){
                st.remove(0);
                st.remove(st.size() - 1);
                for(int j = 0; j < st.size(); j++){
                    res += st.get(j);
                }
                while(!st.isEmpty()){
                    st.pop();
                }
                continue;
            }
        }
        // for(int i = st.size() - 1; i >= 0; i--){
        //     System.out.print(st.get(i) + " ");
        // }
        System.out.println(res);
        return res;
    }
}