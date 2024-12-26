import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class Day5 {

  public static int part1(String[] input) {
    int max = 0;
    for (String s : input) {
      String binary = "";
      for (int i = 0; i < 10; i++) {
        if (s.charAt(i) == 'F' || s.charAt(i) == 'L') {
          binary = binary + "0";
        } else if (s.charAt(i) == 'B' || s.charAt(i) == 'R') {
          binary = binary + "1";
        }
      }
      int row = Integer.parseInt(binary.substring(0, 7), 2);
      int column = Integer.parseInt(binary.substring(7, 10), 2);
      int id = (row * 8) + column;
      max = Math.max(max, id);
    }
    return max;
  }

  public static int part2(String[] input) {
    int[] ids = new int[771];
    int result = 0;
    for (int i = 0; i < 771; i++) {
      String binary = "";
      for (int j = 0; j < 10; j++) {
        if (input[i].charAt(j) == 'F' || input[i].charAt(j) == 'L') {
          binary = binary + "0";
        } else if (input[i].charAt(j) == 'B' || input[i].charAt(j) == 'R') {
          binary = binary + "1";
        }
      }
      int row = Integer.parseInt(binary.substring(0, 7), 2);
      int column = Integer.parseInt(binary.substring(7, 10), 2);
      int id = (row * 8) + column;
      ids[i] = id;
    }
    quicksort(ids, 0, ids.length - 1);
    for (int i = 1; i < ids.length - 1; i++) {
      if (!(ids[i - 1] == ids[i] - 1 && ids[i] + 1 == ids[i + 1])) {
        result = ids[i];
      }
    }
    return result - 1;
  }

  public static void quicksort(int[] a, int s, int e) {
    if (s < e) {
      int l = s;
      int r = e;
      int p = a[(l + e) / 2];
      do {
        while (a[l] < p) {
          l++;
        }
        while (p < a[r]) {
          r--;
        }
        if (l <= r) {
          int t = a[l];
          a[l] = a[r];
          a[r] = t;
          l++;
          r--;
        }
      } while (l <= r);
      quicksort(a, s, r);
      quicksort(a, l, e);
    }
  }

  public static void main(String args[]) {
    File inputText = new File("input.txt");
    String[] input = reader(inputText, 771);
    System.out.println(part2(input));
  }

  public static String[] reader(File input, int lines) {
    String[] result = new String[lines];
    try {
      Scanner reader = new Scanner(input);
      for (int i = 0; i < result.length; i++) {
        result[i] = reader.nextLine();
      }
    } catch (FileNotFoundException x) {
      System.out.println("File not found");
    }
    return result;
  }

}
