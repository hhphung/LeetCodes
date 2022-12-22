class Solution {
    public static boolean isSubsequence(String s, String t) {
        if(s.length() <=0){
            return true;
        }
        if(t.length()<=0) return false;
        int i = 0;
        for(int j = 0; j < t.length(); j ++){
            if(i>= s.length()){
                return true;
            }
            char find = s.charAt(i);
            char comp = t.charAt(j);
            if(find == comp){
                i++;
            }
        }
        return i== s.length();
    }
    
}
