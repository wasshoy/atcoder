const main = (arg) => {
  const inputs = arg.trim().split('\n');
  const [a, b] = inputs[0].split(' ').map(v => Number.parseInt(v));
  const n = Number.parseInt(`${a}${b}`);
  if (Number.isInteger(Math.sqrt(n))) {
    console.log('Yes');
  } else {
    console.log('No');
  }
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));