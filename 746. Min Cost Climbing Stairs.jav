class Solution {
    public static int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        if (n == 0)
            return 0;
        if (n == 1)
            return cost[1];
        int[] minCost = new int[n+1];
        minCost[n] = 0;
        minCost[n-1] = cost[n-1];
        for (int i = minCost.length-3; i >=0; i -- ) {
            minCost[i] = cost[i] + Math.min(minCost[i+1], minCost[i+2]);

        }
        return Math.min(minCost[0], minCost[1]);


    }
}
