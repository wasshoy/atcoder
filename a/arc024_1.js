const main = (arg) => {
  const inputs = arg.trim().split('\n');
  const [L, R] = inputs[0].split(' ').map(v => Number.parseInt(v));
  const l = inputs[1].split(' ').map(v => Number.parseInt(v));
  const r = inputs[2].split(' ').map(v => Number.parseInt(v));
  const left = Array(40-10+1).fill(0);
  const rigtht = Array(40-10+1).fill(0);
  for (let size of l) {
    left[size-10] += 1;
  }
  for (let size of r) {
    rigtht[size-10] += 1;
  }
  let ans = 0;
  for (let i=0; i < 31; i++) {
    ans += Math.min(left[i], rigtht[i]);
  }
  console.log(ans);
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));