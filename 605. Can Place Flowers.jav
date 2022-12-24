class Solution {
    public static boolean canPlaceFlowers(int[] flowerbed, int n) {
        if(n<=0){
            return true;
        }
        if(flowerbed.length<=1){
            if(n>1){
                return false;
            }
            if(flowerbed[0] == 0){
                return  true;
            }
            return false;
        }
        int i  = 0;
        // first index;
        if(flowerbed[i] == 0 && flowerbed[i+1] == 0){
            flowerbed[i] = 1;
            n-=1;
        }
        //from 1 to length-1;
        while(n > 0 && i < flowerbed.length-1){
            for(i = 1 ; i < flowerbed.length-1; i ++){
                if(flowerbed[i] == 0 ){
                    if(flowerbed[i-1] == 0 && flowerbed[i+1] == 0){
                        flowerbed[i] = 1;
                        n-=1;
                    }
                }
            }
        }

        // last index
        if(flowerbed[i] ==0){
            if(flowerbed[i-1] == 0){
                flowerbed[i] =1;
                n-=1;
            }
        }


        return n <=0;
    }
   
}
