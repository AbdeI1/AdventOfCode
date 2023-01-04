import java.util.*;
import java.io.*;

class Day1Code {
  static String[] reader() throws FileNotFoundException {
    return new Scanner(new File("Day1input.txt")).useDelimiter("\\Z").next().split("\n");
  }
  static void part1() throws FileNotFoundException {
    String[] f = reader();
    int[] a = Arrays.stream(f).mapToInt(s -> s.length() == 0 ? -1 : Integer.parseInt(s)).toArray();
    int ans = -1, s = 0;
    for(int i : a) {
      if(i == -1) {
        ans = Math.max(ans, s);
        s = 0;
        continue;
      }
      s += i;
    }
    System.out.println(ans);
  }
  static void part2() throws FileNotFoundException {
    String[] f = reader();
    int[] a = Arrays.stream(f).mapToInt(s -> s.length() == 0 ? -1 : Integer.parseInt(s)).toArray();
    List<Integer> ans = new ArrayList<>();
    int s = 0;
    for(int i : a) {
      if(i == -1) {
        ans.add(s);
        s = 0;
        continue;
      }
      s += i;
    }
    ans.add(s);
    ans.sort(Comparator.reverseOrder());
    System.out.println(ans.get(0) + ans.get(1) + ans.get(2));
  }
  public static void main(String[] args) throws FileNotFoundException {
    part1();
    part2();
  }
}
