use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
  let mut buf = String::with_capacity(8);
  std::io::stdin().read_line(&mut buf)?;
  let num: usize = buf.trim_end().parse()?;
  let sum: usize = (1..=num).sum();

  println!("{}", sum);

  Ok(())
}
