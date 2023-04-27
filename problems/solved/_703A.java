import java.util.Scanner;

public class _703A {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t, m, c, x, y;
        m = 0; c = 0;
        t = in.nextInt();
        while (t-->0) {
            x = in.nextInt(); y = in.nextInt();
            if (x < y) {
                c++;
            } else if (x > y) {
                m++;
            } else {
                continue;
            }
        }
        String ans;
        if (m > c) {
            ans = "Mishka";
        } else if (c > m) {
            ans = "Chris";
        } else {
            ans = "Friendship is magic!^^";
        }
        System.out.println(ans);
        in.close();
    }
}