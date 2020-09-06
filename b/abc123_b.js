function main(arg) {
  const lines = arg.trim().split('\n');
  const INF = Math.pow(10, 100);
  const times = lines.map(Number);
  const ceilTimes = times.map((v) => parseInt(Math.ceil(v / 10) * 10));
  const sum = (acc, v) => acc + v;
  let ans = INF;
  for (let i = 0; i < 5; i++) {
    let sumTimes = 0;
    sumTimes += ceilTimes.reduce(sum) - ceilTimes[i];
    sumTimes += times[i];
    ans = Math.min(ans, sumTimes);
  }
  console.log(ans);
}
main(require('fs').readFileSync('/dev/stdin', 'utf8'));
