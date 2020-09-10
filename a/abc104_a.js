const main = (arg) => {
  const lines = arg.trim().split('\n');
  const R = Number.parseInt(lines[0]);
  console.log(R < 1200 ? 'ABC' : R < 2800 ? 'ARC' : 'AGC');
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));
