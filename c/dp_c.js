const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const LIR = (inputs, start, n) => Array(n).fill().map((_, i) => LI(inputs[start+i]));
const AR = (n, ini) => Array(n).fill(ini);

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const n = I(inputs[0]);
    const a = LIR(inputs, 1, n);
    // dp[i+1][j] : i 日目に 活動 j を選んだ場合の i+1 日目の幸福度の最大値
    const dp = Array(n+1).fill().map(() => Array(3).fill(0));
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < 3; j++) {
        for (let k = 0; k < 3; k++) {
          if (j == k) continue;
          dp[i+1][k] = Math.max(dp[i+1][k], dp[i][j] + a[i][k]);
        }
      }
    }
    console.log(Math.max(...dp[n]));
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));