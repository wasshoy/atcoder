const main = (arg) => {
  const inputs = arg.trim().split('\n');
  const s = inputs[0];
  let ans = '';
  const m = new Map();
  for (let [k, v] of [['O', '0'], ['D', '0'], ['I', '1'], ['Z', '2'], ['S', '5'], ['B', '8']]) {
    m.set(k, v);
  }
  for (let c of s) {
    ans += m.has(c) ? m.get(c) : c;
  }
  console.log(ans);
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));