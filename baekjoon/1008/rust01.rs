fn main() {
  let mut buf = String::new();
  std::io::stdin().read_line(&mut buf).unwrap();

  let inputs = buf
          .split_whitespace()
          .map(|num: &str| num.parse::<f64>().unwrap()).collect::<Vec<f64>>();
  println!("{}", inputs[0] / inputs[1]);
}
