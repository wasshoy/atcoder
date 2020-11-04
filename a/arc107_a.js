const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const [a, b, c] = inputs[0].split(' ').map(v => BigInt(v));
    const mod = 998244353n;
    let ans = 1n;
    ans = ans * (a*(a+1n)/2n % mod) % mod;
    ans = ans * (b*(b+1n)/2n % mod) % mod;
    ans = ans * (c*(c+1n)/2n % mod) % mod;
    console.log(String(ans));
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));