const main = (arg) => {
  const lines = arg.trim().split('\n');
  const n = Number.parseInt(lines[0]);
  let ans = [];
  for (let i = 1; i <= Number.parseInt(Math.sqrt(n)); i++) {
    if (n % i === 0) {
      ans.push(i);
      ans.push(n / i);
    }
  }
  
  ans.sort((a, b) => a - b);
  ans = Array.from(new Set(ans));
  ans.forEach(elem => console.log(elem));
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));
