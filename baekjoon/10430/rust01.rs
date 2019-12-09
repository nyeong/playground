fn main() {
  let mut buf = String::new();
  std::io::stdin().read_line(&mut buf).unwrap();

  let inputs = buf
          .split_whitespace()
          .map(|num: &str| num.parse::<i32>().unwrap()).collect::<Vec<i32>>();
  let a = inputs[0];
  let b = inputs[1];
  let c = inputs[2];
  println!("{}", (a + b) % c);
  println!("{}", (a % c + b % c) % c);
  println!("{}", (a * b) % c);
  println!("{}", (a % c * b % c) % c);
}
