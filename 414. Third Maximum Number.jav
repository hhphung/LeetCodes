import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

class Solution {
    public int thirdMax(int[] nums) {
        HashSet<Integer> remove  = new HashSet<>();
        for(Integer i: nums){
            remove.add(i);
        }
        int[] result = new int[remove.size()];
        int i = 0;
        for(Integer j: remove){
            result[i] = j;
            i++;
        }
        Arrays.sort(result);
        if(result.length<3){
            return result[result.length-1];
        }
        return result[result.length-3];

    }
}
