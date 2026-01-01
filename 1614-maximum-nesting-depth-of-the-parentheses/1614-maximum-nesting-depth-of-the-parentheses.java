class Solution {
    public int maxDepth(String s) {
        Stack<Character> st = new Stack<>();
        String res = "";
        int maxc = 0;
        int c = 0;
        for(int i = 0; i < s.length(); i++){
            // int c = 0;
            if(s.charAt(i) == '(' || s.charAt(i) == ')'){
                if(s.charAt(i) == '('){
                    st.push(s.charAt(i));
                    c += 1;
                }
                else if(s.charAt(i) == ')'){
                    st.remove(st.size() - 1);
                    c -= 1;
                }
            }
            maxc = Math.max(maxc , c);
        }
        System.out.println(maxc);
        return maxc;
    }
}