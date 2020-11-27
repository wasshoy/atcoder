use proconio::input;

fn main() {
    input! {
        n:u32,
    }
    let mut ans = 1;
    for i in 1..10 {
        ans = 111 * i;
        if ans >= n {
            break;
        }
    }
    println!("{}", ans);
}
