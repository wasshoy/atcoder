const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const LIR = (inputs, start, n) => Array(n).fill().map((_, i) => LI(inputs[start+i]));
const AR = (n, ini) => Array(n).fill(ini);
const ARR = (n, m, ini) => Array(n).fill().map(() => Array(m).fill(ini));

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const n = I(inputs[0]);
    const [d, x] = LI(inputs[1]);
    const a = LIR(inputs, 2, n);
    let ans = x;
    for (let ai of a) {
      ans += Math.floor((d-1)/ai) + 1;
    }
    console.log(ans);
};

main(require('fs').readFileSync('/dev/stdin', 'utf8'));