import java.lang.reflect.Array;
import java.util.ArrayList;

class Solution {
    public static int maxProfit(int[] prices) {
        int ans = 0;
        int min = prices[0];
        int max = prices[0];
        for(int i = 1; i < prices.length; i ++){
            if(prices[i] < min){
                min = prices[i];
                max = prices[i];
            }
            if(prices[i] > max){
                max = prices[i];
                ans = Math.max(ans, max - min);
            }
        }
        return ans;
