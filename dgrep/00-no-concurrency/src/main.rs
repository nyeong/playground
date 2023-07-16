use std::collections::HashMap;
use std::fs::{self, File};
use std::path::{Path, PathBuf};
use std::{env, fmt, io};

fn main() -> io::Result<()> {
    let (pattern, paths) = parse_arg(env::args())?;
    let mut results = HashMap::new();

    let paths = find_files(&paths)?;

    for path in paths {
        let patterns = find_pattern(&pattern, &path)?;
        results.insert(path, patterns);
    }

    for (filename, lines) in results.into_iter() {
        if lines.is_empty() {
            continue;
        }

        println!("{}", filename.to_str().unwrap());
        for line in lines {
            println!("{}", line);
        }
    }

    Ok(())
}

fn parse_arg(mut arg: env::Args) -> io::Result<(String, Vec<String>)> {
    // skip the name
    arg.next();

    let pattern = arg.next().ok_or(io::Error::new(
        io::ErrorKind::InvalidInput,
        "no pattern given",
    ))?;
    let paths = arg.collect();

    Ok((pattern, paths))
}

struct Line {
    text: String,
    line_number: usize,
}

impl fmt::Display for Line {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}:{}", self.line_number, self.text)
    }
}

fn find_pattern<P>(pattern: &str, path: P) -> io::Result<Vec<Line>>
where
    P: AsRef<Path>,
{
    let lines = read_lines(path)?;
    let mut results = vec![];

    for (line_number, line) in lines.enumerate() {
        if let Ok(line) = line {
            if line.contains(pattern) {
                results.push(Line {
                    line_number,
                    text: line,
                })
            }
        }
    }

    Ok(results)
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    use std::io::BufRead;
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn find_files(paths: &Vec<String>) -> io::Result<Vec<PathBuf>> {
    let mut stack = vec![];
    let mut files = vec![];

    for path in paths {
        let path = {
            let mut p = PathBuf::new();
            p.push(path);
            p
        };
        if path.is_dir() {
            stack.push(path);
        } else {
            files.push(path);
        }
    }

    while let Some(dir) = stack.pop() {
        for entry in fs::read_dir(dir)? {
            let entry = entry?;
            let path = entry.path();
            if path.is_dir() {
                stack.push(path)
            } else {
                files.push(path)
            }
        }
    }

    Ok(files)
}
