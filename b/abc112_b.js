const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const LIR = (inputs, start, n) => Array(n).fill().map((_, i) => LI(inputs[start+i]));
const AR = (n, ini) => Array(n).fill(ini);
const ARR = (n, m, ini) => Array(n).fill().map(() => Array(m).fill(ini));

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const [n, T] = LI(inputs[0]);

    let cost = Infinity;
    for (let i = 0; i < n; i++) {
      let [ci, ti] = LI(inputs[i+1]);
      if (ti <= T && ci < cost) cost = ci;
    }
    console.log(cost == Infinity ? 'TLE':cost);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));