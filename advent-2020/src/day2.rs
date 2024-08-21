use std::io::Read;

use itertools::Itertools;
use lazy_static::lazy_static;
use regex::Regex;

use crate::utils::read_lines;

// #[derive(Debug)]
pub struct Line<'a> {
    min: usize,
    max: usize,
    car: &'a str,
    pass: &'a str,
}

pub fn extract_line(input: &str) -> Line {
    lazy_static! {
        static ref RE: Regex = Regex::new(r"^(?P<min>\d{1,2})-(?P<max>\d{1,2}) (?P<car>.): (?P<pass>.*)$").unwrap();
    }
    RE.captures(input).map(|cap| {
        let min = cap.name("min").map(|login| login.as_str());
        let max = cap.name("max").map(|login| login.as_str());
        let car = cap.name("car").map(|login| login.as_str());
        let pass = cap.name("pass").map(|login| login.as_str());

        Line {
            min: min.expect("0").parse::<usize>().unwrap(),
            max: max.expect("1").parse::<usize>().unwrap(),
            car: car.expect("oups"),
            pass: pass.expect("oups"),
        }
    }).expect("oups")
}

pub fn test_line1(input: &str) -> bool {
    let line = extract_line(input);
    let value = line.pass.matches(line.car).count();
    line.min <= value && value <= line.max
}


pub fn test_line2(input: &str) -> bool {
    let line = extract_line(input);
    let data = line.pass.as_bytes();
    let c = line.car.as_bytes()[0];
    data[line.min - 1] != data[line.max - 1] && (data[line.min - 1] == c || data[line.max - 1] == c)
}

pub fn solve1(n: usize) -> usize {
    let filter = match n {
        1 => { test_line1 }
        2 => { test_line2 }
        _ => { panic!("oups") }
    };
    if let Ok(lines) = read_lines("src/day2.txt") {
        return lines
            .filter_map(|x| {
                if let Ok(line) = x {
                    return Some(filter(line.as_str()));
                }
                None
            })
            .count();
    }
    panic!("oups")
}


pub fn day2_benchmark() {
    println!("{:?}", solve1(1));
    println!("{:?}", solve1(2));

    timeit!({
        solve1(1);
    });
    timeit!({
        solve1(2);
    });
}