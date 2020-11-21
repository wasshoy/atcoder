use proconio::input;
use std::cmp::min;

fn main() {
    input! {
        n: u32,
        a: u32,
        b: u32,
    };
    let max_num = min(a, b);
    let min_num = if n >= a + b { 0 } else { a + b - n };
    println!("{} {}", max_num, min_num);
}
