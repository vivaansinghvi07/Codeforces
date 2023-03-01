import java.io.*;
import java.util.*;

public class _1791G1 {
  public static void main(String[] args) throws IOException {
    Reader in = new Reader();
    int cases = in.nextInt();
    while (cases --> 0) {
      int n = in.nextInt();
      int coins = in.nextInt();
      int[] costs = in.nextIntArr(n);
      int moves = 0;
      while (coins >= 0) {
        coins -= findMin(costs);
        moves++;
      }
      System.out.println(moves-1);
    }
  }

  public static int findMin(int[] costs) {
    int min = Integer.MAX_VALUE;
    int index = 0;
    for (int i = 0; i < costs.length; i++) {
      if (costs[i] == -1) {
        continue;
      }
      if (costs[i] + i + 1 <= min) {
        index = i;
        min = costs[i] + i + 1;
      }
    }
    costs[index] = -1;
    return min;
  }
}

class Reader {
  private BufferedReader br;
  private StringTokenizer str;
  public Reader () {
    br = new BufferedReader(new InputStreamReader(System.in));
  }
  public String nextToken() throws IOException { 
    while (str == null || !str.hasMoreElements()) { 
      str = new StringTokenizer(br.readLine());
    } 
    return str.nextToken(); 
  } 
  public int nextInt() throws IOException {
    return Integer.parseInt(this.nextToken());
  }
  public char[] nextCharArr() throws IOException {
    return nextToken().toCharArray();
  }
  public int[] nextIntArr(int n) throws IOException {
    int[] out = new int[n];
    for (int i = 0; i < n; i++) {
      out[i] = nextInt();
    }
    return out;
  }
  public int[] nextIntArr() throws IOException {
    String[] str = br.readLine().split("\\s+");
    int[] inp = new int[str.length];
    for (int i = 0; i < str.length; i++) {
      inp[i] = Integer.parseInt(str[i]);
    }
    return inp;
  }
  public long[] nextLongArr() throws IOException {
    String[] str = br.readLine().split("\\s+");
    long[] inp = new long[str.length];
    for (int i = 0; i < str.length; i++) {
      inp[i] = Long.parseLong(str[i]);
    }
    return inp;
  }
  public String nextLine() throws IOException {
    return br.readLine();
  }
  public long nextLong() throws IOException {
    return Long.parseLong(this.nextToken());
  }
  public double nextDouble() throws IOException {
    return Double.parseDouble(this.nextToken());
  }
}