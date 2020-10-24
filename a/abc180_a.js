const main = (arg) => {
  const lines = arg.trim().split('\n');
  const [n, a, b] = lines[0].split(' ').map(v => Number.parseInt(v));
  console.log(n - a + b);
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));
