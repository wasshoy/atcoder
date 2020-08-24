'use strict';

function main(arg) {
  const input = arg.trim().split('\n');
  const d = Number(input[0]);
  const diff = 25 - d;
  let ans = 'Christmas';
  if (diff > 0) {
    ans = ans + ' Eve'.repeat(diff);
  }
  console.log(ans);
}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));
