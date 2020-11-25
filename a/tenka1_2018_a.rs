use proconio::input;

fn main() {
    input! {
        s:String,
    }
    let ans = if s.len() == 2 {
        s
    } else {
        s.chars().rev().collect()
    };
    println!("{}", ans);
}
