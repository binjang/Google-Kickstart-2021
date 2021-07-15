import java.util.*;
import java.io.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 1; i < t + 1; i++) {
            int[] grid = new int[9];
            
            int g1 = sc.nextInt();
            grid[0] = g1;
            int g2 = sc.nextInt();
            grid[1] = g2;
            int g3 = sc.nextInt();
            grid[2] = g3;
            int g4 = sc.nextInt();
            grid[3] = g4;
            int g6= sc.nextInt();
            grid[5] = g6;
            int g7 = sc.nextInt();
            grid[6] = g7;
            int g8 = sc.nextInt();
            grid[7] = g8;
            int g9 = sc.nextInt();
            grid[8] = g9;
            int g5;
            
            int[] ave = new int[4];
            int[] acount = new int[4];
            int s1 = (g1 + g9);
            ave[0] = s1;
            int s2 = (g2 + g8);
            ave[1] = s2;
            int s3 = (g3 + g7);
            ave[2] = s3;
            int s4 = (g4 + g6);
            ave[3] = s4;
            
            int score = 0;
            int [] counts = new int[4];
            for(int j = 0; j < 4; j++){
                int count = 0;
                acount[j] = 0;
                for(int k = 0; k < 4; k++){
                    if(ave[k] == ave[j]) acount[j]++;
                }
                Arrays.sort(acount);
                count += acount[3];
                if(g1 + g3 == (2 * g2)) count++;
                if(g1 + g7 == (2 * g4)) count++;
                if(g9 + g3 == (2 * g6)) count++;
                if(g9 + g7 == (2 * g8)) count++;
                counts[j] = count;
            }
            Arrays.sort(counts);

            System.out.println("Case #" + i + ": " + counts[3]);
        }
    }
}
