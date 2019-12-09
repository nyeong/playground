use std::{io, error};

fn main() -> Result<(), Box<dyn error::Error>>{
  let mut buf = String::new();
  io::stdin().read_line(&mut buf)?;

  let mut nums = buf.split_whitespace()
                .map(|token| token.parse::<i32>().unwrap())
                .collect::<Vec<i32>>();
  nums.sort();

  println!("{}", nums[1]);

  Ok(())
}
