const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const n = Number.parseInt(inputs[0]);
    const a = inputs[1].split(' ').map(v => Number.parseInt(v));
    a.sort((a, b) => a - b);
    let ans = 2;
    let cnt = 0;
    for (let i = 2; i < Number.parseInt(a.slice(-1))+1; i++) {
      let now_cnt = 0;
      for (let v of a) {
        if (v % i == 0) now_cnt++;
      }
      if (now_cnt > cnt) {
        cnt = now_cnt;
        ans = i;
      }
    }
    console.log(ans);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));