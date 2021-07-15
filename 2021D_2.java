import java.util.*;
import java.io.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 1; i < t + 1; i++) {
            int N = sc.nextInt();
            long C = sc.nextInt();
            
            long[][] intvls = new long[2][N];
            long min = Long.MAX_VALUE - 1;
            long max = 0;
            
            for(int j = 0; j < N; j++){
                long j1 = sc.nextInt();
                long j2 = sc.nextInt();
                
                intvls[0][j] = j1;
                intvls[1][j] = j2;
                
                if(j1 < min) min = j1;
                if(j2 > max) max = j2;
            }
            
            long[] counts = new long[(int)(max - min) + 1];
            
            for(int j = 0; j < N; j++){
                long lwr = intvls[0][j];
                long upr = intvls[1][j];
                for(long k = lwr + 1; k < upr; k++){
                    counts[(int)(k - min)]++;
                }
            }
            Arrays.sort(counts);
            long res = N;
            for(int j = (int)Math.min(C, counts.length); j > -1; j--){
                res+= counts[j];
            }
            System.out.println("Case #" + i + ": " + res);
        }
    }
}
