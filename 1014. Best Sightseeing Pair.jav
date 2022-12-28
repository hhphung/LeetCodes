import java.lang.reflect.Array;
import java.util.ArrayList;

class Solution {
    public static int maxScoreSightseeingPair(int[] values) {
    int sum = 0;
    int val = values[0];
    int j = 0;
    for(int i = 1; i < values.length; i ++){
        int a = val + j;
        int b = values[i] - i;
        sum = Math.max(sum, a+b);
        if(values[i] + i > a){
            val = values[i];
            j = i;
        }

    }

    return sum;
}
   
}
