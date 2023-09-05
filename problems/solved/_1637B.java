import java.util.Scanner;
public class _1637B {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        while (t-- > 0) {
            int n = scan.nextInt();
            int ans = n * n * (n + 1) / 2 - n * (n + 1) * (2 * n + 1) / 6 + n * (n + 1) / 2;
            for (int i = 0; i < n; i++) {
                if (scan.nextInt() == 0) {
                    ans += (n - i) * (i + 1);
                }
            }
            System.out.println(ans);
        }
        scan.close();
    }
}