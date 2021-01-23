const main = (arg) => {
  const inputs = arg.trim().split('\n');
  const [a, b] = inputs[0].split(' ').map(v => Number.parseInt(v));
  const n = Number.parseInt(`${a}${b}`);
  for (let i=1; i <= 1000; i++) {
    if (i*i === n) {
      console.log('Yes');
      return;
    }
  }
  console.log('No');
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));