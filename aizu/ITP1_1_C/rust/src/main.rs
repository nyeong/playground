use std::io;

fn main() -> io::Result<()> {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer)?;
    let numbers: Vec<usize> = buffer
        .split_whitespace()
        .map(|token| token.parse::<usize>().expect("Numbers need"))
        .collect();

    if numbers.len() != 2 {
        panic!("Need 2 numbers");
    }

    let rect = Rectangle {
        width: numbers[0],
        height: numbers[1],
    };

    println!("{} {}", rect.area(), rect.round());

    Ok(())
}

struct Rectangle {
    width: usize,
    height: usize,
}

trait Shape {
    fn area(&self) -> usize;
    fn round(&self) -> usize;
}

impl Shape for Rectangle {
    fn area(&self) -> usize {
        self.width * self.height
    }

    fn round(&self) -> usize {
        2 * self.width + 2 * self.height
    }
}
