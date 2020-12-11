const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const LIR = (inputs, start, n) => Array(n).fill().map((_, i) => LI(inputs[start+i]));
const AR = (n, ini) => Array(n).fill(ini);
const ARR = (n, m, ini) => Array(n).fill().map(() => Array(m).fill(ini));


const isPower = (n) => {
  if (n === 1) return true;
  for (let i = 2; Math.pow(n, 1.0/i) >= 2.0; i++) {
    const iThRoot = Math.pow(n, 1.0/i);
    if (iThRoot - Math.floor(iThRoot) == 0.0) return true;
  return false;
}
}

const main = (arg) => {
  const inputs = arg.trim().split('\n');
  const x = I(inputs[0]);
  let ans = 1;
  for (let b = 1; b < x+1; b++) {
    for (let p = 2; p < 11; p++) {
      if (ans < b**p && b**p <= x) ans = b**p;
    }
  }
  console.log(ans);
};

main(require('fs').readFileSync('/dev/stdin', 'utf8'));