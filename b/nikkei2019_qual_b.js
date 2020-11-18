const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const n = Number.parseInt(inputs[0]);    
    const a = inputs[1].split('');    
    const b = inputs[2].split('');    
    const c = inputs[3].split('');    
    let ans = 0;
    for (let i = 0; i < n; i++) {
      if (a[i] == b[i] && a[i] == c[i]) continue;
      else if ((a[i] == b[i] && a[i] != c[i]) || (b[i] == c[i] && b[i] != a[i]) || (c[i] == a[i] && c[i] != b[i])) ans++;
      else ans += 2;
    }
    console.log(ans);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));