import java.util.*;

class Solution {
    public static int countValidWords(String sentence) {
        int count = 0;
        String[] splited = sentence.split(" ");
        for(String s: splited) {
            boolean found = false;
            if (s.length() > 0) {
                int i = 0;
                for (i=0; i < s.length() ; i++) {
                    char c = s.charAt(i);
                    if (Character.isDigit(c)) break;
                    if((c=='!' || c=='.' || c==',') && i!=s.length()-1) break;
                    if(c=='-' && (i==0 || i==s.length()-1 || !Character.isLetter(s.charAt(i-1)) || !Character.isLetter(s.charAt(i+1)))) break;
                    if (c == '-') {
                        if (found) break;
                        found = true;
                    }
                }
                if (i == s.length()) count++;

            }
        }
        return count;
}


}
