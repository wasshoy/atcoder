function main(arg) {
  const lines = arg.trim().split('\n');
  let nums = lines[0].split(' ');
  nums.sort((a, b) => {
    return b - a;
  });
  nums = nums.map((elem) => Number(elem));
  const ans = nums[0] * 10 + nums[1] + nums[2];
  console.log(ans);
}
main(require('fs').readFileSync('/dev/stdin', 'utf8'));
