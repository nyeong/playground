use std::{io, error};

fn main() -> Result<(), Box<dyn error::Error>>{
  let mut buf = String::new();
  io::stdin().read_line(&mut buf)?;

  let nums = buf.split_whitespace()
                .map(|token| token.parse::<i32>().unwrap())
                .collect::<Vec<i32>>();
  let mut time = Time::new(nums[0], nums[1]);

  time.rewind(0, 45);

  println!("{} {}", time.hours(), time.minutes());

  Ok(())
}

/// Time is a struct that can contain a time info between 00:00 ~ 23:59
struct Time {
  minutes: i32
}

impl Time {
  fn new(hours: i32, minutes: i32) -> Self {
    assert!(hours < 24);
    assert!(minutes < 60);

    Self {
      minutes: ( hours * 60 + minutes ) as i32
    }
  }

  fn rewind(&mut self, hours: i32, minutes: i32) {
    let rhs = hours * 60 + minutes;

    self.minutes -= rhs as i32;

    if self.minutes < 0 {
      self.minutes += 60 * 24;
    }
  }

  fn hours(&self) -> u8 {
    ( self.minutes / 60 ) as u8
  }

  fn minutes(&self) -> u8 {
    ( self.minutes % 60 ) as u8
  }
}
