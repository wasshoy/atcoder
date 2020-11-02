const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const n = Number.parseInt(inputs[0]);
    if (n % 2 === 0) {
      console.log('White');
    } else {
      console.log('Black');
    }
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));