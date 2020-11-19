const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const AR = (n, ini) => Array(n).fill(ini);

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const s = inputs[0].split('');
    const rest = 15 - s.length;
    let win = s.filter(result => result == 'o').length + rest;
    console.log(win >= 8 ? 'YES' : 'NO');
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));