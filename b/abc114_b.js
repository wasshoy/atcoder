const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const s = inputs[0].split('');
    let ans = Infinity;
    for (let i = 0; i < s.length-2; i++) {
      let num = Number.parseInt(s[i] + s[i+1] + s[i+2]);
      ans = Math.min(ans, Math.abs(753 - num));
    }
    console.log(ans);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));