use std::fs;
use std::cmp::max;

pub fn reader() -> Vec<String> {
  let f = fs::read_to_string("input.txt").expect("Unable to read file");
  let mut v: Vec<String> = f.split("\n").map(str::to_string).collect();
  v = v[..v.len()-1].to_vec();
  v
}

pub fn part1() {
  let f = reader();
  let mut ans = 0;
  let mut s = 0;
  for l in f {
    if l == "" {
      ans = max(ans, s);
      s = 0;
      continue;
    }
    s += l.parse::<i32>().unwrap();
  }
  println!("{}", ans);
}

pub fn part2() {
  let f = reader();
  let mut ans: Vec<i32> = vec![];
  let mut s = 0;
  for l in f {
    if l == "" {
      ans.push(s);
      s = 0;
      continue;
    }
    s += l.parse::<i32>().unwrap();
  }
  ans.sort();
  ans.reverse();
  println!("{}", ans[0] + ans[1] + ans[2]);
}

fn main() {
  part1();
  part2();
}
