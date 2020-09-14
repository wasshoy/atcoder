const main = (arg) => {
  const lines = arg.trim().split('\n');
  const [a, b] = lines[0].split(' ').map((v) => Number.parseInt(v));
  let ans = 1;
  ans += a <= b ? a - 1 : a - 2;
  console.log(ans);
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));
