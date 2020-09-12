const main = (arg) => {
  const lines = arg.trim().split('\n');
  const N = Number.parseInt(lines[0]);
  console.log(N % 2 == 0 ? N : 2 * N);
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));
