const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const LIR = (inputs, start, n) => Array(n).fill().map((_, i) => LI(inputs[start+i]));
const AR = (n, ini) => Array(n).fill(ini);
const ARR = (n, m, ini) => Array(n).fill().map(() => Array(m).fill(ini));

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const N = I(inputs[0]);
    let isOk = true;
    let word = inputs[1];
    let vocSet = new Set([word]);
    for (let i = 0; i < N-1; i++) {
      let wi = inputs[i+2];
      if (!vocSet.has(wi) && word.slice(-1) == wi[0]){
        word = wi;
        vocSet.add(wi);
      } else {
        isOk = false;
        break;
      }
    }
    console.log(isOk? 'Yes' : 'No');
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));