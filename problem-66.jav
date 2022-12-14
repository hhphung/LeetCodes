import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public static int[] plusOne(int[] digits) {
        int length = digits.length;
        int[] result = new int[length+1];


        int last_of_result = length;
        for(int i = length-1; i >=0; i --){
            result[last_of_result]=digits[i];
            last_of_result--;
        }
        last_of_result = result.length;
        result[last_of_result-1]+=1;
        for(int i = last_of_result-1; i >=1; i --){
            if(result[i]%10 == 0){
                result[i] = 0;
                result[i-1] +=1;
            }
            else {
                return Arrays.copyOfRange(result, 1, last_of_result);
            }
        }


        return result;
    }


}
