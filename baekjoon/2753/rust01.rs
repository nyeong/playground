use std::{io, error};

fn main() -> Result<(), Box<dyn error::Error>>{
  let mut buf = String::new();
  io::stdin().read_line(&mut buf)?;

  let year = buf.trim_end().parse::<u16>()?;

  println!("{}", if is_leafyear(year) {1} else {0});

  Ok(())
}

fn is_leafyear(num: u16) -> bool {
  num % 4 == 0 && num % 100 != 0 || num % 400 == 0
}
