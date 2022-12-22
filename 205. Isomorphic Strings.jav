import java.util.HashMap;
import java.util.Hashtable;
import java.util.Map;

class Solution {
    public static boolean isIsomorphic(String s, String t) {
        if(s == null || s.length() <= 1) return true;
        Map<Character, Character> map = new HashMap<>();
        for(int i = 0; i < s.length(); i ++){
            char in_s = s.charAt(i);
            char in_t = t.charAt(i);
            if(map.containsKey(in_s)){
                if(map.get(in_s).equals(in_t))
                    continue;
                else
                    return false;
            }else {
                if (!map.containsValue(in_t))
                    map.put(in_s, in_t);
                else return false;
            }
            }
        return true;
        }
  
}
