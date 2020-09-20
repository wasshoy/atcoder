const main = (arg) => {
  const lines = arg.trim().split('\n');
  const s = lines[0].split('');
  let ans = '';
  let count = 0;
  let now = s[0];
  s.forEach((c) => {
    if (now === c) count++;
    else {
      ans += now + count.toString(10);
      now = c;
      count = 1;
    }
  });
  ans += now + count.toString(10);
  console.log(ans);
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));
