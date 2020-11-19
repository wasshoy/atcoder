const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const [n, k] = LI(inputs[0]);
    const h = LI(inputs[1]);
    const costs = Array(n).fill(Infinity);
    costs[0] = 0;
    for (let i = 0; i < n; i++) {
      for (let j = 1; j < k+1; j++) {
        if (i + j < n) {
          costs[i + j] = Math.min(costs[i + j], costs[i] + Math.abs(h[i] - h[i+j]));
        }
      }
    }
    console.log(costs[n-1]);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));