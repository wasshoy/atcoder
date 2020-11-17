const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const n = Number.parseInt(inputs[0]);
    const a = inputs[1].split(' ').map(v => Number.parseInt(v));
    let now = 1;
    let ans = 0;
    let is_ok = false;
    for (let i of a) {
      if (i == 1) is_ok = true;
      if (i == now) {
        now++;
      } else {
        ans++;
      }
    }
    if (is_ok) console.log(ans);
    else console.log(-1);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));