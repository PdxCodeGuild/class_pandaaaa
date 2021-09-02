let rotation = parseInt(prompt("enter the rotation: "));
const userString = prompt("enter a string: ");

let lowerLetters = "abcdefghijklmnopqrstuvwxyz";
let upperLetters = lowerLetters.toUpperCase();

let convertedString = "";

if (rotation < 0) {
  lowerLetters = lowerLetters.split("").reverse().join("");
  upperLetters = upperLetters.split("").reverse().join("");
  rotation = Math.abs(rotation);
}

for (i = 0; i < userString.length; i++) {
  index = lowerLetters.indexOf(userString[i]);

  if (index !== -1) convertedString += lowerLetters[(index + rotation) % 26];
  else if (index === -1) {
    index = upperLetters.indexOf(userString[i]);
    if (index === -1) convertedString += userString[i];
    else convertedString += upperLetters[(index + rotation) % 26];
  }
}

console.log(convertedString);
