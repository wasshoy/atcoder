const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const n = I(inputs[0]);
    const h = LI(inputs[1]);
  
    let costs = Array(n).fill(Infinity);
    costs[0] = 0;
    costs[1] = Math.abs(h[0] - h[1]);

    for (let i = 2; i < n; i++) {
      costs[i] = Math.min(
        costs[i-1] + Math.abs(h[i] - h[i-1]),
        costs[i-2] + Math.abs(h[i] - h[i-2]));
    }
    console.log(costs[n-1]);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));