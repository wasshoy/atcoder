use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        n: u32,
        s: Chars,
    };
    let mut red_cnt = 0;
    for c in s {
        if c == 'R' {
            red_cnt += 1
        };
    }
    let ans = if red_cnt > n - red_cnt { "Yes" } else { "No" };
    println!("{}", ans);
}
