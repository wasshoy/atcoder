use proconio::input;

fn main() {
    input! {
        a:u32,
        b:u32,
        x:u32,
    }
    println!("{}", if a <= x && x <= a + b { "YES" } else { "NO" });
}
