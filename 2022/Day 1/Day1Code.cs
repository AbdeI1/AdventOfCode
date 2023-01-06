using System;
using System.Collections.Generic;

class Day1Code {
  static string[] reader() {
    string[] f = System.IO.File.ReadAllLines("./Day1input.txt");
    return f;
  }
  static void part1() {
    string[] f = reader();
    int ans = -1;
    int s = 0;
    foreach(string l in f) {
      if(l == "") {
        ans = Math.Max(ans, s);
        s = 0;
        continue;
      }
      s += Int32.Parse(l);
    }
    Console.WriteLine(ans);
  }
  static void part2() {
    string[] f = reader();
    List<int> a = new List<int>();
    int s = 0;
    foreach(string l in f) {
      if(l == "") {
        a.Add(s);
        s = 0;
        continue;
      }
      s += Int32.Parse(l);
    }
    a.Sort();
    a.Reverse();
    Console.WriteLine(a[0] + a[1] + a[2]);
  }
  static void Main(string[] args) {
    part1();
    part2();
  }
}
