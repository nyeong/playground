fn main() {
  let mut buf = String::new();
  std::io::stdin().read_line(&mut buf).unwrap();

  let inputs = buf
          .split_whitespace()
          .map(|num: &str| num.parse::<i32>().unwrap()).collect::<Vec<i32>>();
  println!("{}", inputs[0] + inputs[1]);
  println!("{}", inputs[0] - inputs[1]);
  println!("{}", inputs[0] * inputs[1]);
  println!("{}", inputs[0] / inputs[1]);
  println!("{}", inputs[0] % inputs[1]);
}
