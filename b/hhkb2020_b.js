const main = (arg) => {
  const lines = arg.trim().split('\n');
  const [h, w] = lines[0].split(' ').map(v => Number.parseInt(v));
  const [_, ...s] = lines;
  let ans = 0;
  for (let i = 0; i < h; i++){
    for (let j = 0; j < w; j++) {
      if (i+1 < h) {
        if ((s[i][j] === ".") && (s[i+1][j] === ".")) {
          ans += 1;
        }
      }
      if (j+1 < w) {
        if ((s[i][j] === ".") && (s[i][j+1] === ".")) {
          ans += 1;
        }
      }
    }
  }
  console.log(ans);
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));
