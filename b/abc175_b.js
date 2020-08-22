'use strict';

const is_ok = (l) => {
  l.sort((x, y) => y - x); // 昇順ソート
  return l[0] - l[1] < l[2] && l[0] !== l[1] && l[1] !== l[2];
};
const main = (arg) => {
  const input = arg.trim().split('\n');
  const n = Number(input[0]);
  const l = input[1].split(' ').map(Number);
  let ans = 0;
  if (n < 3) {
    ans = 0;
  } else {
    for (let i = 0; i < n; i++) {
      for (let j = i + 1; j < n; j++) {
        for (let k = j + 1; k < n; k++) {
          if (is_ok([l[i], l[j], l[k]])) ans++;
        }
      }
    }
  }
  console.log(ans);
};

main(require('fs').readFileSync('/dev/stdin', 'utf8'));
