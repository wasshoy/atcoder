const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const LIR = (inputs, start, n) => Array(n).fill().map((_, i) => LI(inputs[start+i]));
const AR = (n, ini) => Array(n).fill(ini);
const ARR = (n, m, ini) => Array(n).fill().map(() => Array(m).fill(ini));

// 20m AC
const main = (arg) => {
  const inputs = arg.trim().split('\n');
  const s = inputs[0];
  let isOk = true;

  if (s.charAt(0) !== 'A') isOk = false;

  let Ccnt = 0;
  let Cind = 0;
  for (let i = 2; i < s.length - 1;i++) {
    if (s.charAt(i) === 'C')  {
      Ccnt++;
      Cind = i;
    }
  }
  if (Ccnt !== 1) isOk = false;

  for (let i = 0; i < s.length; i++) {
    if (i === 0 || i === Cind) continue;
    if (s.charAt(i).toLowerCase() !== s.charAt(i)) isOk = false;
  }
  console.log(isOk ? 'AC' : 'WA');
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));