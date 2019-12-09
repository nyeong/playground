use std::error::Error;
use std::io::{BufReader, stdin, BufWriter, stdout};

fn main() -> Result<(), Box<dyn Error>> {
  let mut reader = BufReader::new(stdin());
  let mut writer = BufWriter::new(stdout());

  let mut buf = String::new();
  reader.read_line(&mut buf);
  let num: u32 = buf.trim_end().parse()?;
  println!("{}", num);

  Ok(())
}
