use std::error::Error;

fn main() -> Result<(), Box<dyn Error>>{
  let mut buf = String::new();
  std::io::stdin().read_line(&mut buf)?;
  let num: usize = buf.trim_end().parse()?;

  for i in 1..=9 {
    println!("{} * {} = {}", num, i, num * i);
  }

  Ok(())
}
