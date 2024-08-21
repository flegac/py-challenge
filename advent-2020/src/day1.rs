use std::cmp::{max, min, Ordering};

use itertools::{Itertools, sorted};

use crate::utils::read_lines;

type Int = u32;
type Int2 = u64;

struct Input<'a> {
    filename: &'a str,
    target: Int,
}

const BASIC: Input = Input {
    filename: "src/day1.txt",
    target: 2020,
};

const HARD1: Input = Input {
    filename: "src/bad_case.txt",
    target: 600006,
};
const HARD2: Input = Input {
    filename: "src/bad_case2.txt",
    target: 6,
};


fn solve_fast(input: Input, n: usize) -> Option<Int2> {
    let items = sorted(parse_file(&input.filename)).rev().collect_vec();
    solve(&items, input.target, n)
}

fn solve(items: &[Int], target: Int, n: usize) -> Option<Int2> {
    if n == 1 {
        find_index(items, target).map(|index| items[index] as Int2)
    } else {
        (0..items.len())
            .filter(|i| items[*i] <= target)
            .map(|i| (i, solve(&items[i + 1..], target - items[i], n - 1)))
            .find(|(i, x)| x.is_some())
            .map(|(i, x)| x.map(|x| x * items[i] as Int2))
            .flatten()
    }
}

fn find_index(items: &[Int], value: Int) -> Option<usize> {
    if items.is_empty() || items[items.len() - 1] > value || value > items[0] {
        return None;
    }
    let j = items.len() / 2;
    match items[j].cmp(&value) {
        Ordering::Equal => { Some(j) }
        Ordering::Less => { find_index(&items[0..j], value) }
        Ordering::Greater => {
            find_index(&items[j + 1..], value)
                .map(|index| index + j + 1)
        }
    }
}

pub fn day1_benchmark() {
    // println!("{} {}",
    //          solve1(2).expect("No solution"),
    //          solve1(3).expect("No solution"));
    // timeit!({
    //     solve1(2);
    //     solve1(3);
    // });

    println!("{} {}",
             solve_fast(BASIC, 2).expect("No solution"),
             solve_fast(BASIC, 3).expect("No solution")
    );
    timeit!({
         solve_fast(BASIC, 2);
         solve_fast(BASIC, 3);
    });

    timeit!({
         solve_fast(HARD1, 2);
         solve_fast(HARD1, 3);
    });

    timeit!({
         solve_fast(HARD2, 2);
         solve_fast(HARD2, 3);
    });
}


fn solve1(input: Input, n: usize) -> Option<Int2> {
    parse_file(&input.filename)
        .into_iter()
        .combinations(n)
        .filter(|vec| vec.iter().sum::<Int>() == input.target)
        .find(|vec| vec.iter().sum::<Int>() == input.target)
        .map(|vec| vec.iter().product::<Int>() as Int2)
}

fn solve2(input: Input, n: usize) -> Option<Int2> {
    parse_file(&input.filename)
        .iter()
        .copied()
        .tuple_combinations()
        .find(|(a, b, c)| a + b + c == input.target)
        .map(|(a, b, c)| (a * b * c) as Int2)
}

fn parse_file(filename: &str) -> Vec<Int> {
    let mut all = vec![];
    if let Ok(lines) = read_lines(filename) {
        for line in lines {
            if let Ok(value) = line {
                all.push(value.parse::<Int>().unwrap());
            }
        }
    }
    return all;
}
