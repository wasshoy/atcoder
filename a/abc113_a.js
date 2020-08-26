function main(arg) {
  input_line = arg.trim().split('\n');
  [x, y] = input_line[0].split(' ').map((elem) => parseInt(elem));
  console.log(x, y);
  console.log(x + y / 2);
}
main(require('fs').readFileSync('/dev/stdin', 'utf8'));
