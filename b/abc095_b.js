const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const IR = (inputs, start, n) => Array(n).fill().map((_, i) => I(inputs[start+i]));
const LIR = (inputs, start, n) => Array(n).fill().map((_, i) => LI(inputs[start+i]));
const AR = (n, ini) => Array(n).fill(ini);
const ARR = (n, m, ini) => Array(n).fill().map(() => Array(m).fill(ini));

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const [n, x] = LI(inputs[0]);
    const m = IR(inputs, 1, n);
    let ans = n;
    const sum = (acc, cur) => acc + cur;
    let kona = x - m.reduce(sum);
    m.sort((a, b) => a - b);
    let rest = Number.parseInt(kona / m[0]);
    console.log(ans+rest);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));