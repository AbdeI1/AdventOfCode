open Util

let f = List.map (int_of_string) (UtilM.read_words "Day1input.txt")

let part1 =
  let rec counter cur count l =
    match l with
    | [] -> count
    | h::t -> if h > cur then counter h (count + 1) t else counter h count t
  in counter (1000000) 0 f

let part2 = 
  let rec counter count l =
    match l with
    | h1::h2::h3::h4::t -> if h4 > h1 then counter (count + 1) (h2::h3::h4::t) else counter count (h2::h3::h4::t)
    | _ -> count
  in counter 0 f

let () = print_string ((string_of_int part1) ^ "\n")
let () = print_string ((string_of_int part2) ^ "\n")
