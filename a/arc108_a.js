const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const AR = (n, ini) => Array(n).fill(ini);

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const [s, p] = LI(inputs[0]);
    let ans = 'No';
    for (let i = 1; i < (Number.parseInt(Math.sqrt(p))+1); i++) {
      if (i*(s-i) == p) ans = 'Yes';
    }
    console.log(ans);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));