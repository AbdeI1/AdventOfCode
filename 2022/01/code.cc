#include <bits/stdc++.h>
#include <string.h>

#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

vector<string> reader() {
  ifstream f("input.txt");
  stringstream ss;
  ss << f.rdbuf();
  string s = ss.str();
  vector<string> v;
  int i;
  while ((i = s.find("\n")) != -1) {
    v.push_back(s.substr(0, i));
    s = s.substr(i + 1);
  }
  v.pop_back();
  return v;
}

void part1() {
  vector<string> f = reader();
  int ans = 0;
  int s = 0;
  for (string l : f) {
    if (l == "") {
      ans = s > ans ? s : ans;
      s = 0;
      continue;
    }
    s += atoi(l.c_str());
  }
  cout << ans << endl;
}

void part2() {
  vector<string> f = reader();
  vector<int> ans = {};
  int s = 0;
  for (string l : f) {
    if (l == "") {
      ans.push_back(s);
      s = 0;
      continue;
    }
    s += atoi(l.c_str());
  }
  ans.push_back(s);
  sort(ans.begin(), ans.end());
  reverse(ans.begin(), ans.end());
  cout << ans[0] + ans[1] + ans[2] << endl;
}

int main() {
  part1();
  part2();
}
