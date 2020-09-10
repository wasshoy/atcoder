function main(arg) {
  const lines = arg.trim().split('\n');
  const [A, B] = lines[0].split(' ').map(Number);
  console.log((A - 1) * (B - 1));
}
main(require('fs').readFileSync('/dev/stdin', 'utf8'));
