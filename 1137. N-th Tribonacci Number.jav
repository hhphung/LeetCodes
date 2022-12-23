class Solution {
        public static int tribonacci(int n) {
            if(n<=1){
                return n;
            }
            if(n==2){
                return 1;
            }
            int[] list = new int[n+1];
            list[0] = 0;
            list[1]= 1;
            list[2] = 1;
            for(int i =3; i <= n; i ++){
                list[i] = list[i-1] + list[i-2] + list[i-3] ;
            }
            return list[n-1] + list[n-2] + list[n-3];
        }
   
}
