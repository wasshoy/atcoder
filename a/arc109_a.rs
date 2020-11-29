use proconio::input;
use std::cmp::min;

fn main() {
    input! {
        a:u32,
        b:u32,
        x:u32,
        y:u32,
    }
    if a == b {
        println!("{}", x);
    } else if a == b + 1 {
        println!("{}", x);
    } else {
        let steps = if a <= b { b - a } else { a - b };
        if a <= b {
            let ans = steps * min(y, 2 * x) + x;
            println!("{}", ans);
        } else {
            let ans = (steps - 1) * min(y, 2 * x) + x;
            println!("{}", ans);
        }
    }
}
