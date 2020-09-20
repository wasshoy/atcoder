const main = (arg) => {
  const lines = arg.trim().split('\n');
  const [x1, y1, x2, y2] = lines[0].split(' ').map((v) => Number.parseInt(v));
  const x = x2 - x1,
    y = y2 - y1;
  const x3 = x2 - y,
    y3 = y2 + x,
    x4 = x1 - y,
    y4 = y1 + x;
  console.log(`${x3} ${y3} ${x4} ${y4}`);
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));
