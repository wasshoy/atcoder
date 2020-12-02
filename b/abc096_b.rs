use proconio::input;
fn main() {
    input! {
        a:i32,
        b:i32,
        c:i32,
        k:u32,
    }
    let ans: i32;
    let two: i32 = 2;
    if a >= b && a >= c {
        ans = a * two.pow(k) + b + c;
    } else if b >= a && b >= c {
        ans = b * two.pow(k) + a + c;
    } else {
        ans = c * two.pow(k) + a + b;
    }
    println!("{}", ans);
}
