import java.util.*;
import java.io.*;

class code {
  static String[] reader() throws FileNotFoundException {
    return new Scanner(new File("input.txt")).useDelimiter("\\Z").next().split("\n");
  }

  static Map<Character, Integer> D = new HashMap<>() {
    {
      put('A', 0);
      put('B', 1);
      put('C', 2);
      put('X', 1);
      put('Y', 2);
      put('Z', 3);
    }
  };

  static void part1() throws FileNotFoundException {
    String[] f = reader();
    int ans = 0;
    for (String s : f) {
      ans += D.get(s.charAt(2));
      if ((D.get(s.charAt(0)) + 1) % 3 == D.get(s.charAt(2)) - 1)
        ans += 6;
      else if (D.get(s.charAt(0)) == D.get(s.charAt(2)) - 1)
        ans += 3;
    }
    System.out.println(ans);
  }

  static void part2() throws FileNotFoundException {
    String[] f = reader();
  }

  public static void main(String[] args) throws FileNotFoundException {
    part1();
    part2();
  }
}
