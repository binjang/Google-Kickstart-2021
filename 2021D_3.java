import java.util.*;
import java.io.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 1; i < t + 1; i++) {
            int N = sc.nextInt();
            int M = sc.nextInt();
            int[][] tests = new int[2][N];
            int count = 0;
            
            for(int j = 0; j < N; j++){
                int j1 = sc.nextInt();
                tests[0][j] = j1;
                int j2 = sc.nextInt();
                tests[1][j] = j2;
                
                count += j2 - j1 + 1;
            }
            
            int[] probs = new int[count];
            int idx = 0;
            
            for(int j = 0; j < N; j++){
                for(int k = tests[0][j]; k <= tests[1][j]; k++){
                    probs[idx] = k;
                    idx++;
                }
            }
            
            int[] stds = new int[M];
            int[] ans = new int[M];
            
            for(int j = 0; j < M; j++){
                stds[j] = sc.nextInt();
            }
            
            int start = 0;
            int end = count - 1;
            
            for(int j = 0; j < M; j++){
                idx = 0;
                if (stds[j] <= probs[start]){
                    ans[j] = probs[start];
                    probs[start] = -1;
                    start++;
                }else if(stds[j] >= probs[end]){
                    ans[j] = probs[end];
                    probs[end] = -1;
                    end--;
                }else{
                    int idxl = 0;
                    while(stds[j] - probs[idx] > 0){
                        if(probs[idx] != -1){
                            idxl = idx;
                        }
                        idx++;
                    }
                    int lwr = probs[idxl];
                    int upr = probs[idx];
                    int res = (upr - stds[j]) < (stds[j] - lwr) ? upr : lwr;
                    ans[j] = res;
                    if((upr - stds[j]) < (stds[j] - lwr)){
                        probs[idx] = -1;
                    } else probs[idxl] = -1;
                }
            }
            System.out.println("Case #" + i + ": " + Arrays.toString(ans).replace("[", "").replace("]", "").replace(",", ""));
        }
    }
}
