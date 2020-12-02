const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const LIR = (inputs, start, n) => Array(n).fill().map((_, i) => LI(inputs[start+i]));
const AR = (n, ini) => Array(n).fill(ini);
const ARR = (n, m, ini) => Array(n).fill().map(() => Array(m).fill(ini));

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const [n, m, x] = LI(inputs[0]);
    const a = new Set(LI(inputs[1]));
    let l = 0, r = 0;
    for (let ai of a) {
      if (ai < x) l++;
      else r++;
    }
    console.log(Math.min(l, r));
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));