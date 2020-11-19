const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const LIR = (inputs, start, n) => Array(n).fill().map((_, i) => LI(inputs[start+i]));
const AR = (n, ini) => Array(n).fill(ini);
const ARR = (n, m, ini) => Array(n).fill().map(() => Array(m).fill(ini));

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const [n, W] = LI(inputs[0]);
    const w = [], v = [];
    for (let i = 0; i < n; i++) {
      const [wi, vi] = LI(inputs[i+1]);
      w.push(wi);
      v.push(vi);
    }

    // dp[i+1][j] : 重さ j の上限の元で 品物 i を選んだ場合の価値の最大値
    const dp = ARR(n+1, W+1, 0);
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < W+1; j++) {
        if (j - w[i] >= 0) {  // 品物 i を選べる
          dp[i+1][j] = Math.max(dp[i][j], dp[i][j-w[i]] + v[i]);
        } else { // 品物 i を選べない
          dp[i+1][j] = Math.max(dp[i+1][j], dp[i][j]);
        }
      }
    }
    let ans = Math.max(dp[n][W]);
    console.log(ans);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));