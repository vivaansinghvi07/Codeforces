import java.io.*;
import java.util.*;

public class _1895B {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int testcases = scan.nextInt();
        for (int i = 0; i<testcases; i++){
            int n = scan.nextInt();
            int[] arr = new int[n*2];
            for (int j = 0; j<n * 2; j++){
                arr[j] = scan.nextInt();
            }
            Arrays.sort(arr);
            int dist = 0;
            for (int iii = 0; iii < arr.length - 1; iii++) {
                if (iii == arr.length / 2 - 1) {
                    continue;
                }
                dist += arr[iii+1] - arr[iii];
            }
            System.out.println(dist);
            for (int ii = 0; ii < arr.length / 2; ii++) {
                System.out.println(arr[ii] + " " + arr[arr.length - ii - 1]);
            } 
        }
    }
}
