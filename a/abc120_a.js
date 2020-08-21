'use strict';

const main = (arg) => {
  const input = arg.trim().split('\n');
  const [a, b, c] = input[0].split(' ');
  let ans = 0;
  if (b >= a * c) {
    ans = c;
  } else {
    ans = Math.floor(b / a);
  }
  console.log(ans);
};

main(require('fs').readFileSync('/dev/stdin', 'utf8'));
