const main = (arg) => {
  const inputs = arg.trim().split('\n');
  const n = Number.parseInt(inputs[0]);
  const a1 = inputs[1].split(' ').map(v => Number.parseInt(v));
  const a2 = inputs[2].split(' ').map(v => Number.parseInt(v));
  const sumReducer = (acc, curV) => acc + curV;
  let ans = 0;
  for (let i=0; i < n; i++) {
    ans = Math.max(ans, a1.slice(0, i+1).reduce(sumReducer, 0) + a2.slice(i, n).reduce(sumReducer, 0));
  }
  console.log(ans);
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));