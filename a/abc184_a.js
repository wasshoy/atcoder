const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const AR = (n, ini) => Array(n).fill(ini);

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const [a, b] = LI(inputs[0]);
    const [c, d] = LI(inputs[1]);
    console.log(a*d - b*c);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));