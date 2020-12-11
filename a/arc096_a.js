const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const LIR = (inputs, start, n) => Array(n).fill().map((_, i) => LI(inputs[start+i]));
const AR = (n, ini) => Array(n).fill(ini);
const ARR = (n, m, ini) => Array(n).fill().map(() => Array(m).fill(ini));

const main = (arg) => {
  const inputs = arg.trim().split('\n');
  const [a, b, c, x, y] = LI(inputs[0]);
  let ans = 0;
  let rest = 0;
  if (2*c < a+b) {
    ans += 2 * c * Math.min(x, y);
    rest = Math.max(x, y) - Math.min(x, y);
    if (y < x) {  // A が残る
      if (2*c < a) { ans += 2 * c * rest; } else { ans += a * rest; }
    } else {  // B が残る
      if (2*c < b) { ans += 2 * c * rest; } else { ans += b * rest; }
    }
  } else {
    ans += a*x + b*y;
  }
  console.log(ans);
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));