import java.util.Scanner;

public class _1826B {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t, n;
        t = scan.nextInt();
        while (t-- > 0) {
            n = scan.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = scan.nextInt();
            }
            if (n / 2 == 0) {
                System.out.println(0);
                continue;
            }
            int[] diffs = new int[(int) (n / 2)];
            for (int i = 0; i < (int) (n / 2); i++) {
                diffs[i] = Math.abs(arr[n - i - 1] - arr[i]);
            }
            System.out.println(gcfArray(diffs));
        }
    }

    public static void penIs(int n) {
        String output = "";
        while (n-- > 0) {
            output += "=";
        }
        System.out.println("8" + output + "D");
    }

    public static int gcf(int a, int b) {
        if (b == 0) {
            return a;
        } else if (a == 0) {
            return b;
        } else {
            return gcf(b, a % b);
        }
    }

    public static int gcfArray(int[] arr) {
        int g = arr[0];
        for (int a : arr) {
            /* implemented in part (a) */
            g = gcf(g, a);
        }
        return g;
    }
}