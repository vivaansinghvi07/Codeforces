import java.io.*;
import java.util.*;

public class _1791G2 {
  public static void main(String[] args) throws IOException {
    Reader in = new Reader();
    int cases = in.nextInt();
    String answer = "Answer: ";
    while (cases --> 0) {
      int n = in.nextInt();
      int coins = in.nextInt();
      Teleporter[] spots = new Teleporter[n];
      for (int i = 0; i < n; i++) {
        spots[i] = new Teleporter(in.nextInt(), i, n);
      }
      int moves = 0;
      /* coins -= findMin(spots);
      if (coins < 0) {
        answer += moves + " ";
        continue;
      }
      else {
        moves++;
      } */
      Arrays.sort(spots, new Comparator<Teleporter>() {
        public int compare(Teleporter a, Teleporter b) {
          return Integer.compare(Math.min(a.cost1, a.cost2), Math.min(b.cost1, b.cost2));
        }
      });
      boolean done = false;
      for (Teleporter t : spots) {
        if (t.used) {
          continue;
        }
        else {
          int cost = t.cost2;
          if (t.cost1 <= t.cost2) {
            cost = t.cost1;
            done = true;
          }
          t.used = true;
          if (coins - cost < 0) {
            break;
          }
          else {
            moves++;
            coins -= cost;
          }
        }
      }
      if (!done) {
        Arrays.sort(spots, new Comparator<Teleporter>() {
          public int compare(Teleporter a, Teleporter b) {
            return Integer.compare(Math.abs(a.cost1 - a.cost2), Math.abs(b.cost1 - b.cost2));
          }
        });
        moves--;
        for (Teleporter t : spots) {
          if (t.used) {
            coins += t.cost2;
            coins -= t.cost1;
            break;
          }
        }
        if (coins >= 0) {
          answer += (moves + 1) + " ";
        }
        else {
          answer += moves + " ";
        }
      }
      else {
        answer += (moves) + " ";
      }
    }
    System.out.println(answer);
  }
  public static int findMin(Teleporter[] spots) {
    int min = Integer.MAX_VALUE;
    int index = 0;
    for (int i = 0; i < spots.length; i++) {
      if (spots[i].cost1 < min) {
        min = spots[i].cost1;
        index = i;
      }
    }
    spots[index].used = true;
    return min;
  }
}

class Teleporter {
  public int cost1;
  public int cost2;
  public int index;
  public boolean used;
  public Teleporter (int cost, int index, int n) {
    this.cost1 = cost + index + 1;
    this.cost2 = cost + n - index;
    this.index = index;
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