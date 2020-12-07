const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const LIR = (inputs, start, n) => Array(n).fill().map((_, i) => LI(inputs[start+i]));
const AR = (n, ini) => Array(n).fill(ini);
const ARR = (n, m, ini) => Array(n).fill().map(() => Array(m).fill(ini));

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const [a, b, ...rest] = LI(inputs[0]);
    let k_hitoketame = Number.parseInt(inputs[0].split(' ')[3].slice(-1));  // k がとても大きい場合もあるので、偶数・奇数判定のための一桁目だけとる
    if (k_hitoketame%2 == 0) {
      console.log(a-b);
    } else {
      console.log(b-a);
    }
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));