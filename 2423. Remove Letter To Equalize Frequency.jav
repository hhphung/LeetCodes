import java.util.*;

class Solution {
    public static boolean equalFrequency(String word) {
        int[] cnt = new int[26];

        for(int i = 0; i < word.length(); i ++) {
            char c = word.charAt(i);
            cnt[c - 'a']++;
        }
        for(int i = 0; i < word.length(); i ++ ){
            int index = word.charAt(i) -'a';
            cnt[index]-=1;
            HashSet<Integer> list = new HashSet<>();
            for (int j = 0; j < word.length(); j ++) {
                int a = word.charAt(j) -'a';
                if (cnt[a] != 0) {
                    list.add(cnt[a]);
                }

            }
            if (list.size() == 1) {
                return true;
            }
            cnt[index]+=1;
        }



       return false;
    }

  
}
