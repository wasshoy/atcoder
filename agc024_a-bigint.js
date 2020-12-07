const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const LIR = (inputs, start, n) => Array(n).fill().map((_, i) => LI(inputs[start+i]));
const AR = (n, ini) => Array(n).fill(ini);
const ARR = (n, m, ini) => Array(n).fill().map(() => Array(m).fill(ini));

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const [a, b, ...rest] = LI(inputs[0]);
    let k = inputs[0].split(' ')[3];
    if (k > Number.MAX_SAFE_INTEGER) { // k が大きすぎるとき、BigIntとして扱う
      k = BigInt(k);
    }
    const divisor = k > Number.MAX_SAFE_INTEGER ? 2n : 2;
    if (k%divisor == 0) {
      console.log(a-b);
    } else {
      console.log(b-a);
    }
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));