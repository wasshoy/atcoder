use proconio::input;

fn main() {
    input! {
        a:u32,
        b:u32,
    }
    let ans: &str = if a + b == 15 {
        "+"
    } else if a * b == 15 {
        "*"
    } else {
        "x"
    };
    println!("{}", ans);
}
