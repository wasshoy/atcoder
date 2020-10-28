import * as fs from 'fs';
const inputs = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n');
const N = +inputs[0];
const D = inputs.splice(1).map(v => v.split(' '));
let have_thrice_zorome = false;
for (let i = 0; i < N-2; i++) {
    for (let j = 0; j < 3; j++) {
        if (D[i+j][0] === D[i+j][1]) {
            have_thrice_zorome = true;
        } else {
            have_thrice_zorome = false;
            break;
        }
    }
    if (have_thrice_zorome) {
        break;
    }
}

if (have_thrice_zorome) {
    console.log('Yes');
} else {
    console.log('No');
}