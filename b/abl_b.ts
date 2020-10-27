import * as fs from 'fs';
const main = (arg) => {
  const lines = arg.trim().split('\n');
  const [a, b, c, d] = lines[0].split(' ').map(v => Number.parseInt(v));
  if (b < c || d < a) {
    console.log("No");
  } else {
    console.log("Yes");
  }
};
main(fs.readFileSync('/dev/stdin', 'utf8'));
