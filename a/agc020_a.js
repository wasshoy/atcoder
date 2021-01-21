const main = (arg) => {
  const inputs = arg.trim().split('\n');
  const [n, a, b] = inputs[0].split(' ').map(v => Number.parseInt(v));
  let xa = a;
  let xb = b;
  let turn = true;
  while (xa > 0 && xb <= n) {
    if (turn) {
      if (xa+1 === xb) {
        xa -= 1;
      } else {
        xa += 1;
      }
    } else {
      if (xb-1 === xa) {
        xb += 1;
      } else {
        xb -= 1;
      }
    }
    turn = !turn;
  }

  const ans = xa <= 0 ? 'Borys' : 'Alice';
  console.log(ans);
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));