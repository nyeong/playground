use std::io;

fn main() {
    let (height, width) = get_two_numbers();
    let before_photo = create_photo_from_stdin();
    let min_distance = before_photo.get_min_distance();

    let mut buff = String::new();
    for i in 0..height {
        for j in 0..width {
            if (i as isize) - min_distance >= 0 && before_photo.data[(i - min_distance) as usize][j as usize] == Pixel::Star {
                buff.push('X');
            } else if before_photo.data[i as usize][j as usize] == Pixel::Terran {
                buff.push('#');
            } else {
                buff.push('.');
            }
        }
        buff.push('\n');
    }

    println!("{}", buff);
}

fn get_two_numbers() -> (isize, isize) {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let mut iter = line.split_whitespace();
    let a = iter.next().unwrap().parse::<isize>().unwrap();
    let b = iter.next().unwrap().parse::<isize>().unwrap();
    (a, b)
}

#[derive(Copy, Clone, Debug, PartialEq)]
enum Pixel {
    Air,
    Terran,
    Star,
}

struct Photo {
    data: Vec<Vec<Pixel>>,
}

impl Photo {
    fn get_min_distance(&self) -> isize {
        let mut min_distance = isize::MAX;
        for j in 0..self.data[0].len() {
            let mut count = 0;
            let mut is_meet_star = false;
            for i in 0..self.data.len() {
                match self.data[i][j] {
                    Pixel::Air => {
                        count += 1;
                    }
                    Pixel::Terran => {
                        if is_meet_star {
                            min_distance = std::cmp::min(min_distance, count);
                        }
                        break;
                    }
                    Pixel::Star => {
                        count = 0;
                        is_meet_star = true;
                    }
                }
            }
        }
        min_distance
    }
}

fn create_photo_from_stdin() -> Photo {
    let lines = std::io::stdin().lines();
    let mut data = Vec::new();
    for line in  lines {
        match line {
            Ok(line) => {
                let mut v = Vec::new();
                for c in line.chars() {
                    match c {
                        '.' => v.push(Pixel::Air),
                        '#' => v.push(Pixel::Terran),
                        'X' => v.push(Pixel::Star),
                        _ => panic!(""),
                    }
                }
                data.push(v);
            }
            Err(_) => panic!(""),
        }
    }
    Photo {
        data: data,
    }
}
