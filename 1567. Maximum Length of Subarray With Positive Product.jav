import java.lang.reflect.Array;
import java.util.ArrayList;

class Solution {
    public static  int getMaxLen(int arr[])
    {
        int N = arr.length;
        int Pos = 0;
        int Neg = 0;
        int res = 0;

        for (int i = 0; i < N; i++)
        {
            if (arr[i] == 0)
            {
                Pos = Neg = 0;
            }
            else if (arr[i] > 0)
            {
                Pos += 1;
                if (Neg != 0)
                {
                    Neg += 1;
                }
                res = Math.max(res, Pos);
            }
            else
            {
                Pos = Pos + Neg;
                Neg = Pos - Neg;
                Pos = Pos - Neg;
                
                Neg += 1;
                
                if (Pos != 0)
                {
                    Pos += 1;
                }
                res = Math.max(res, Pos);
            }
        }
        return res;

}
   
}
