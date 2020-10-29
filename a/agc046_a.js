const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const x = Number.parseInt(inputs[0]);
    let m = 1;
    while (360*m % x !== 0) { m++; }
    console.log(360*m / x);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));