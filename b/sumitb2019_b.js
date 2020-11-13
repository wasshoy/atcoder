const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const n = Number.parseInt(inputs[0]);
    let ans;
    if (Number.parseInt(n/1.08) * 1.08 === n) {
      ans = Number.parseInt(n/1.08);
    } else if (Number.parseInt((Number.parseInt(n/1.08)+1) * 1.08) === n) {
      ans = Number.parseInt(n/1.08) + 1;
    } else ans = ':(';
  
    console.log(ans);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));