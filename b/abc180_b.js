const main = (arg) => {
  const lines = arg.trim().split('\n');
  const n = Number.parseInt(lines[0]);
  const x = lines[1].split(' ').map(v => Number.parseInt(v));

  const sum = (acc, v) => acc + v;
  const manhattan = x.map(v => Math.abs(v)).reduce(sum, 0);
  const euclid = Math.sqrt(x.map(v => v*v).reduce(sum, 0));
  const chebyshev = Math.max(...x.map(v => Math.abs(v)));

  console.log(manhattan);
  console.log(euclid);
  console.log(chebyshev);
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));
