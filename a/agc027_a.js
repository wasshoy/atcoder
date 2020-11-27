const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const LIR = (inputs, start, n) => Array(n).fill().map((_, i) => LI(inputs[start+i]));
const AR = (n, ini) => Array(n).fill(ini);
const ARR = (n, m, ini) => Array(n).fill().map(() => Array(m).fill(ini));

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    let [N, x] = LI(inputs[0]);
    const a = LI(inputs[1]);
    const sort_a = a.sort((a, b) => a - b);
    let ans = 0;
    for (let ai of a.slice(0, N-1)) {
      if (x-ai >= 0) {
        ans++;
        x -= ai;
      } else { break; }
    }
if (x == a[N-1]) ans++;
    console.log(ans);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));