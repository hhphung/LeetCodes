import java.util.*;

class Solution {
    public static boolean buddyStrings(String s, String goal) {
        char[] sArray = s.toCharArray();
        char[] goalArray = goal.toCharArray();
        if(s.length()!= goal.length() || s.length()<=0 || goal.length() <=0){
            return false;
        }

        if (s.equals(goal)) {
            HashSet<Character> list = new HashSet<>();
            for(int i = 0; i < s.length(); i++){
                char c = s.charAt(i);
                list.add(c);
            }
            return list.size() < goal.length();
        }

        ArrayList<Integer> index = new ArrayList<>();
        for(int i = 0; i < goal.length(); i ++){
            if(s.charAt(i) != goal.charAt(i)){
                index.add(i);
            }
        }
        if(index.size() != 2){
            return false;
        }
        int i = index.get(0);
        int j = index.get(1);
        if(s.charAt(i) == goal.charAt(j) && s.charAt(j) == goal.charAt(i)){
            return true;
        }


        return false;
    }

  

}
