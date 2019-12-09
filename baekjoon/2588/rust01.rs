fn main() {
  let a = read_nums_from_line();
  let b = read_nums_from_line();

  println!("{}", a * (b % 10));
  println!("{}", a * (b % 100 - b % 10) / 10);
  println!("{}", a * (b % 1000 - b % 100) / 100);
  println!("{}", a * b);
}

fn read_nums_from_line() -> i32 {
  let mut buf = String::new();
  std::io::stdin().read_line(&mut buf).unwrap();

  buf.trim().
  parse::<i32>().unwrap()
}
