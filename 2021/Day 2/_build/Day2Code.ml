open Util
open UtilM

let f = List.map implode (split_by (fun x -> x = '\n') (read_file "Day2input.txt"))

let part1 = 
  let rec helper x y l =
    match l with 
    | [] -> x*y
    | h::t -> 
      let dir::dist_s::[] = List.map implode (split_by (fun x -> x = ' ') (explode h)) in
        let dist = int_of_string dist_s in
          match dir with
          | "forward" -> helper (x + dist) y t
          | "up" -> helper x (y - dist) t
          | "down" -> helper x (y + dist) t
          | _ -> raise (Failure "unexpected input")
  in helper 0 0 f

let part2 = 
  let rec helper x y aim l =
    match l with 
    | [] -> x*y
    | h::t -> 
      let dir::dist_s::[] = List.map implode (split_by (fun x -> x = ' ') (explode h)) in
        let dist = int_of_string dist_s in
          match dir with
          | "forward" -> helper (x + dist) (y + (aim*dist)) aim t
          | "up" -> helper x y (aim - dist) t
          | "down" -> helper x y (aim + dist) t
          | _ -> raise (Failure "unexpected input")
  in helper 0 0 0 f

let () = print_string ((string_of_int part1) ^ "\n")
let () = print_string ((string_of_int part2) ^ "\n")
