function main(arg) {
  const inputLines = arg.trim().split('\n');
  const n = inputLines[0].split('');
  let ans = '';
  n.forEach((c) => {
    if (c === '1') {
      ans += '9';
    } else {
      ans += '1';
    }
  });
  console.log(ans);
}
main(require('fs').readFileSync('/dev/stdin', 'utf8'));
