class Solution {
    public int countGoodSubstrings(String s) {
        char[] a = s.toCharArray();
        int n = a.length;
        int l = 0 , r = 2 , cout = 0;
        while(r < n){
            Set<Character> charset = new LinkedHashSet<>();
           for(int i = l; i <= r; i++){
            charset.add(a[i]);
           }
           if(charset.size() == 3){
            cout++;
           }
           l++;
           r++;
        }
        System.out.println(cout);
        return cout;
    }
}