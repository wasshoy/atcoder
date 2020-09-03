function main(arg) {
  const lines = arg.trim().split('\n');
  const [A, B] = lines[0].split(' ').map((x) => Number(x));
  const res = (A * B) % 2 !== 0 ? 'Yes' : 'No';
  console.log(res);
}
main(require('fs').readFileSync('/dev/stdin', 'utf8'));
