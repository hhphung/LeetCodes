import java.lang.reflect.Array;

class Solution {
    public static int maxProduct(int[] nums) {
        int N = nums.length;
        int max = nums[0];
        int max_temp = nums[0];
        int min_temp = nums[0];
        for(int i = 1; i < N; i ++){
            int a = max_temp * nums[i];
            int b = min_temp * nums[i];
            max_temp = Math.max(Math.max(a,b), nums[i]);
            min_temp = Math.min(Math.min(a,b), nums[i]);
            max = Math.max(max, max_temp);

        }
        return max;

}
    
}
