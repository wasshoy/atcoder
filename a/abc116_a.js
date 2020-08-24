'use strict';

const main = (arg) => {
  const input = arg.trim().split('\n');
  const [ab, bc, ca] = input[0].split(' ').map(Number);
  const ans = (ab * bc) / 2;
  console.log(ans);
};

main(require('fs').readFileSync('/dev/stdin', 'utf8'));
