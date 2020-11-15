const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const s = inputs[1];
    const k = Number.parseInt(inputs[2]);
    const s_k = s[k-1];
    let ans = '';
    for (let si of s) {
      if (si === s_k) {
        ans += si;
      }
      else {
        ans += '*';
      }
    }
    console.log(ans);

  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));