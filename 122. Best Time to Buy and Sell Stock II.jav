 class Solution {
        public static int maxProfit(int[] prices) {
            int sum = 0;
            int max = prices[0];
            int min = prices[0];
            int profit = 0;
            for(int i =1; i < prices.length; i ++){
                if(prices[i] < min){
                    min = prices[i];
                    max = prices[i];
                    sum+= profit;
                    profit=0;
                }
                else if(prices[i] < max){
                    min= prices[i];
                    max = prices[i];
                    sum+= profit;
                    profit = 0;
                }
                else {
                   profit+= prices[i] -max;
                   max = Math.max(max, prices[i]);
                }
            }
            sum+= profit;
    
            return sum;
    
    }
  
    }
