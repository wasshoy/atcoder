use proconio::input;

fn main() {
    input! {
        n:u32,
        h:u32,
        w:u32,
    };
    let ans = (n - h + 1) * (n - w + 1);
    println!("{}", ans);
}
