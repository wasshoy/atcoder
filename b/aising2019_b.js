const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const AR = (n, ini) => Array(n).fill(ini);

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const n = Number.parseInt(inputs[0]);
    const [a, b] = LI(inputs[1]);
    const p = LI(inputs[2]);
    let cnt1 = 0, cnt2 = 0, cnt3 = 0;
    for (let pi of p) {
      if (pi <= a) cnt1++;
      else if (a+1 <= pi && pi <= b) cnt2++;
      else cnt3++;
    }
    console.log(Math.min(...[cnt1, cnt2, cnt3]));
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));