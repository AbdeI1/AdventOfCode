import { readFileSync } from "fs";

function reader() {
  const f = readFileSync("./input.txt", "utf-8");
  let a = f.split("\n");
  a = a.slice(0, -1);
  return a;
}

function part1() {
  const f = reader();
  const a: number[] = f.map((s: string) => (s == "" ? -1 : parseInt(s)));
  let s = 0;
  let ans = -1;
  a.forEach((i) => {
    if (i == -1) {
      ans = Math.max(ans, s);
      s = 0;
    } else {
      s += i;
    }
  });
  console.log(ans);
}

function part2() {
  const f = reader();
  const a: number[] = f.map((s: string) => (s == "" ? -1 : parseInt(s)));
  let s = 0;
  let ans: number[] = [];
  a.forEach((i) => {
    if (i == -1) {
      ans.push(s);
      s = 0;
    } else {
      s += i;
    }
  });
  ans.sort((x, y) => y - x);
  console.log(ans[0] + ans[1] + ans[2]);
}

part1();
part2();
