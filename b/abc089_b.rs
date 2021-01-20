use proconio::input;
fn main() {
    input! {
        n: u32,
        s: [char; n],
    }
    let mut is_four = false;
    for si in s {
        if si == 'Y' {
            is_four = true;
        }
    }
    let ans = if is_four { "Four" } else { "Three" };
    println!("{}", ans);
}
