const main = (arg) => {
  const lines = arg.trim().split('\n');
  const N = Number.parseInt(lines[0]);
  const A = lines[1].split(' ').map((v) => Number.parseInt(v));
  A.sort((a, b) => b - a);
  console.log(A.slice(0) - A.slice(-1));
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));
