use proconio::input;
use proconio::marker::Chars;
fn main() {
    input! {
        _n:u32,
        x:u32,
        s:Chars,
    };
    let mut ans: u32 = x;
    for c in s {
        if c == 'o' {
            ans += 1;
        } else {
            ans = if ans <= 0 { 0 } else { ans - 1 };
        };
    }
    println!("{}", ans);
}
