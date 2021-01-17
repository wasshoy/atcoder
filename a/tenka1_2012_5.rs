use proconio::input;

fn main() {
    input! {
        a:u32,
        b:u32,
        c:u32,
    }
    let mut ans = vec![];
    for i in 1..128 {
        if i%3 == a && i%5 == b && i%7 == c {
            ans.push(i);
        }
    }
    for i in ans {
        println!("{}", i);
    }
}
