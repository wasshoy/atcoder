const I = line => Number.parseInt(line);
const LI = line => line.split(' ').map(v => Number.parseInt(v));
const AR = (n, ini) => Array(n).fill(ini);

const main = (arg) => {
    const inputs = arg.trim().split('\n');
    const s = inputs[0].split('');
    const n = s.length;
    // 貪欲法 ： 前からできるだけ短い文字列で切っていく
    // 最後に 2文字残り、それらが同じである場合、そのまま使う
    // 2文字が直前の 2文字と一致する場合、4文字を 3, 1文字で切って使う
    let k = 0;
    let preWord = '';
    let i = 0;
    while (i < n) {
      let nowWord = s[i];
      if (nowWord == preWord) {
        i++;
        if (i >= n) break;
        nowWord += s[i];
      }
      k++;
      preWord = nowWord;
      i++;
    }
    console.log(k);
  };
  main(require('fs').readFileSync('/dev/stdin', 'utf8'));