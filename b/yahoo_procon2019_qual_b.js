const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const AR = (n, ini) => Array(n).fill(ini);

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const v = [];
    for (let i = 0; i < 4; i++) v.push([]);
    for (let i = 0; i < 3; i++){
      const [ai, bi] = LI(inputs[i]);
      v[ai-1].push(bi-1);
      v[bi-1].push(ai-1);
    }
    let ans = 'YES';
    for (let vi of v) {
      if (vi.length > 2) {
        ans = 'NO';
        break;
      }
    }
    console.log(ans);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));