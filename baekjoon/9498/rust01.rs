use std::{io, error};

fn main() -> Result<(), Box<dyn error::Error>>{
  let mut buf = String::new();
  io::stdin().read_line(&mut buf)?;

  let score = buf.trim_end().parse::<u8>()?;
  let score = match score {
    90..=100 => "A",
    80..=89 => "B",
    70..=79 => "C",
    60..=69 => "D",
  _ => "F"
  };

  println!("{}", score);

  Ok(())
}
