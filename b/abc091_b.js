// 21m AC
const main = (arg) => {
  const inputs = arg.trim().split('\n');
  const n = Number.parseInt(inputs[0]);
  const s = inputs.slice(1, n+1);
  const m = Number.parseInt(inputs[n+1]);
  const t = inputs.slice(n+2, n+2+m);
  const ms = new Map();
  const mt = new Map();
  for (let v of s) {
    if (!ms.get(v)) {
      ms.set(v, 0);
    }
    ms.set(v, ms.get(v)+1);
  }
  for (let v of t) {
    if (!mt.get(v)) {
      mt.set(v, 0);
    }
    mt.set(v, mt.get(v)+1);
  }
  
  let ans = 0;
  ms.forEach((v, k) => {
    if (!mt.get(k)) {
      ans = Math.max(ans, v);
    } else {
      ans = Math.max(ans, v - mt.get(k));
    }
  });
  console.log(ans);
};
main(require('fs').readFileSync('/dev/stdin', 'utf8'));