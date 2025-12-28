class Solution {
    public String makeGood(String s) {
        Stack<Character> st = new Stack<>();
        String res = "";
        for(int i = 0; i < s.length(); i++){
            st.push(s.charAt(i));

            if(st.size() > 1){
                char a = st.get(st.size() - 1);
                char b = st.get(st.size() - 2);
                int c = (int) a;
                int d = (int) b;
                if(c >= 65 && c <= 90){
                    char e = (char) (c + 32);
                    if(c+32 == d){
                        st.remove(st.size() - 1);
                        st.remove(st.size() - 1);
                    }
                }
                if(c >= 97 && c <= 122){
                    if(c - 32 == d){
                        st.remove(st.size() - 1);
                        st.remove(st.size() - 1);
                    }
                }
                
            }
        }
        for(int i = 0; i < st.size(); i++){
            res += st.get(i);
        }
        return res;
    }
}