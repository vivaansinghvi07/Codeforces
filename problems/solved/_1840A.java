import java.util.Scanner;
import java.util.ArrayList;
public class _1840A {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        while (t --> 0) {
            int n = scan.nextInt();
            char[] arr = (scan.next() + " ").toCharArray();
            ArrayList<Character> chars = new ArrayList<Character>();
            char temp = arr[0];
            for (int i = 1; i < n; i++) {
                if (arr[i] != temp) {
                    continue;
                }
                chars.add(temp);
                temp = arr[i+1];
                i++;
            }
            String output = new String();
            for (char c : chars) {
                output += c;
            }
            System.out.println(output);
        }
        scan.close();
    }
}