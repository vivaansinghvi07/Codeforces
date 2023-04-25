import java.util.Scanner;

public class _1822A {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t, n, s, m, x, d;
        t = scan.nextInt();
        while (t --> 0) {
            n = scan.nextInt();
            s = scan.nextInt();
            m = Integer.MIN_VALUE;
            d = -1;
            int[] times = new int[n];
            for (int i = 0; i < n; i++) {
                times[i] = i + scan.nextInt();
            }
            for (int i = 0; i < n; i++) {
                x = scan.nextInt(); 
                if (times[i] <= s && x > m) {
                    m = x;
                    d = i + 1;
                }
            }
            System.out.println(d);
        }
        scan.close();
    }
}
