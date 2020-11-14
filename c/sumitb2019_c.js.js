const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const x = Number.parseInt(inputs[0]);
    let exists = false;
    for (let i = 1; i < 1001; i++) {
      if (100*i <= x && x <= 105*i) {
        exists = true;
        break;
      }
    }
    console.log(exists? 1 : 0);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));