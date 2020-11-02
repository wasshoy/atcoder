const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const [a, v] = inputs[0].split(' ').map(v => Number.parseInt(v));
    const [b, w] = inputs[1].split(' ').map(v => Number.parseInt(v));
    const t = Number.parseInt(inputs[2]);
    const d = Math.abs(a - b);
    let ans;
    if (v > w && d/(v-w) <= t) {
      ans = 'YES';
    } else {
      ans = 'NO';
    }
    console.log(ans);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));