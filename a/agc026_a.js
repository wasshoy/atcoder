const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const LIR = (inputs, start, n) => Array(n).fill().map((_, i) => LI(inputs[start+i]));
const AR = (n, ini) => Array(n).fill(ini);
const ARR = (n, m, ini) => Array(n).fill().map(() => Array(m).fill(ini));

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const n = I(inputs[0]);
    const a = LI(inputs[1]); 
    let ans = 0;
    const nums = Array(new Set(a));
    for (let i = 0; i < n; i++) {
      if (i+1 < n && a[i] == a[i+1]){
        nums.push(nums[nums.length-1] + 1);
        a[i+1] = nums[nums.length - 1];
        ans++;
      }
    }
    console.log(ans);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));