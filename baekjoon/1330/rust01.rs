use std::cmp::Ordering;

fn main() {
  let mut buf = String::new();
  std::io::stdin().read_line(&mut buf).unwrap();
  let nums = buf.trim().split_whitespace()
     .map(|token| token.parse::<i32>().unwrap())
     .collect::<Vec<i32>>();
  let a: i32 = nums[0];
  let b: i32 = nums[1];

  match a.cmp(&b) {
    Ordering::Greater => println!(">"),
    Ordering::Less => println!("<"),
    Ordering::Equal => println!("=="),
  }
}
