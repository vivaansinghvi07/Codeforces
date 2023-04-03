import java.util.Scanner;
public class _230Av1 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int s = scan.nextInt();
        int n = scan.nextInt();

        String ans = "YES";
        while (n --> 0) {
            if (scan.nextInt() < s) {
                s += scan.nextInt();
            } else {
                ans = "NO";
                break;
            }
        }
        System.out.println(ans);
        scan.close();
    }
}