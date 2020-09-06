function main(arg) {
  const lines = arg.trim().split('\n');
  const N = Number(lines[0]);
  const H = lines[1].split(' ').map(Number);
  let ans = 1;
  let maxHeight = H[0];
  for (const hi of H.slice(1)) {
    if (hi >= maxHeight) ans++;
    maxHeight = Math.max(hi, maxHeight);
  }
  console.log(ans);
}
main(require('fs').readFileSync('/dev/stdin', 'utf8'));
