i = 1
while (i <= 200){
  a = Day1input[i, 1]
  j = i + 1
  while (j <= 200){
    b = Day1input[j, 1]
    k = j + 1
    while (k <= 200){
      c = Day1input[k, 1]
      if(a + b + c == 2020){
        print(i)
        print(j)
        print(k)
      }
      k = k + 1
    }
    j = j + 1
  }
  i = i + 1
}
