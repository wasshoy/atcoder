use proconio::input;

fn main() {
    input! {
        n:u32,
    }
    let mut ni = n;
    let mut sn = 0;
    while ni > 0 {
        sn += ni % 10;
        ni /= 10;
    }
    let ans = if n%sn == 0 {"Yes"} else {"No"};
    println!("{}", ans);
}
