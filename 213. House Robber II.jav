class Solution {
    public static int rob(int[] nums) {
        if(nums.length <=1){
            return nums[0];
        }
        int[] take = new int[nums.length];
        int skip = 0;
        take[0] = nums[0];

        for(int i = 1; i < nums.length-1; i++){
            take[i] = skip + nums[i];
            skip = Math.max(skip, take[i-1]);
        }
        int max = Math.max(take[take.length-2] , skip);
        take = new int[nums.length];
        skip = 0;
        take[1] = nums[1];
        for(int i = 2; i < nums.length; i ++){
            take[i] = skip + nums[i];
            skip = Math.max(skip, take[i-1]);
        }
        int i = Math.max(take[take.length-1] , skip);
        max = Math.max(max, i );


        return max;
    }

}
