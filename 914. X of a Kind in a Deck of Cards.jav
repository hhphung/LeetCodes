import java.util.*;
import java.util.Collection;
import java.util.HashMap;

class Solution {
    public static boolean hasGroupsSizeX(int[] deck) {
        HashMap<Integer, Integer> list = new HashMap<>();
        for(Integer i: deck){
            if(list.containsKey(i)){
                int newVal = list.get(i)+1;
                list.replace(i, newVal);

            }
            else{
                list.put(i, 1);
            }
        }
        List<Integer> nums = new ArrayList<>(list.values());
        int min = nums.get(0);
        for(Integer i : nums){
            min = Math.min(min,i);
        }
        for(int i=2; i <= min; i ++){
            if(allDivi(nums,i)){
                return true;
            }
        }


        return false;
    }
    private static boolean allDivi(List<Integer> list, int i) {
        for (int a : list) {
            if (a % i != 0) return false;
        }
        return true;
    }


}
