import java.util.ArrayList;
import java.util.HashSet;
import java.util.Hashtable;

class Solution {
    public static int longestPalindrome(String s) {
        Hashtable<Character, Integer> map = new Hashtable<>();
        for(int i = 0; i < s.length(); i ++){
            char c= s.charAt(i);

            if (map.containsKey(c)){
                map.replace(c, map.get(c)+1);
            }
            else{
                map.put(c, 1);
            }
        }

        int ans = 0;
        boolean odd = false;
        ArrayList<Integer> value = new ArrayList<>(map.values());
        for(Integer i: value){
            if(i%2 == 0){
                ans+=i;
            }else {
                ans += i - 1;
                odd = true;
            }
        }
        ans += odd ? 1 : 0;
        return ans;
}

       
    }
