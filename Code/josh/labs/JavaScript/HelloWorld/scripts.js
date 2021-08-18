console.log("hello from the scripts file");
let list = ["apple", "banana", "pear"];

let listDiv = document.getElementById("list");

for (let i = 0; i < list.length; i++) {
  const element = list[i];
  listDiv.innerText += " " + element;
}
console.debug("console.debug", list);
console.log(list);

console.debug("huh");
