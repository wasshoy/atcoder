// 51
const main = (arg) => {
  const lines = arg.trim().split('\n');
  const S = lines[0];
  let base = 'WBWBWWBWBWBW' + 'WBWBWWBWBWBW' + 'WBWBWWBWBWBW';
  let scales = new Map([
    [0, 'Do'],
    [2, 'Re'],
    [4, 'Mi'],
    [5, 'Fa'],
    [7, 'So'],
    [9, 'La'],
    [11, 'Si'],
  ]);
  let ans;

  for (const i of scales.keys()) {
    // console.log(i);
    // console.log(base.slice(i, i + 20));
    if (base.slice(i, i + 20) === S) {
      ans = scales.get(i);
      break;
    }
  }
  console.log(ans);
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));
