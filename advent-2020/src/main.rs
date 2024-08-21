#[macro_use]
extern crate timeit;

use lazy_static::lazy_static;
use regex::Regex;

use crate::day1::day1_benchmark;
use crate::day2::day2_benchmark;

mod day1;
mod day2;
mod utils;


fn main() {
    day1_benchmark();
    // day2_benchmark();
}

