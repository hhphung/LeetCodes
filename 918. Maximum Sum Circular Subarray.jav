import java.lang.reflect.Array;

class Solution {
    public static int maxSubarraySumCircular(int[] nums) {
        if(nums.length <=1){
            return nums[0];
        }
        int N = nums.length;
        int max = nums[0];
        int min = nums[0];
        int max_num = nums[0];
        int min_num = nums[0];
        int sum = 0;
        for(int i = 1; i < N; i ++){
            max_num +=  nums[i];
            min_num+= nums[i];
            if(nums[i] > max_num){
                max_num =  nums[i];
            }
            if(max_num > max){
                max = max_num;
            }
            if(nums[i] < min_num){
                min_num = nums[i];
            }
            if(min_num < min){
                min = min_num;
            }
        }
        for(int i: nums){
            sum+=i;
        }
        if(sum-min == 0){
            return max;
        }

        for(int i = 1;i < N; i ++){

        }



        return Math.max(max, sum-min);
    }
}
