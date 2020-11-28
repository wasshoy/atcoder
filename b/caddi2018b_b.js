const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const LIR = (inputs, start, n) => Array(n).fill(0).map((_, i) => LI(inputs[start+i]));
const AR = (n, ini) => Array(n).fill(ini);
const ARR = (n, m, ini) => Array(n).fill(0).map(() => Array(m).fill(ini));

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const [N, H, W] = LI(inputs[0]);
    let ans = 0;
    const ab = LIR(inputs, 1, N);
    for (let [a, b] of ab) {
      if (a >= H && b >= W) ans++;
    }
    console.log(ans);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));