// select parent from document
let container_div = document.querySelector("#container");
console.log(container_div)

// loop through 12 times
for (i = 1; i < 13; i++) {
  // creating new element
  let newDiv = document.createElement("div");
  // assigning classes to new element
  newDiv.classList.add(`btn-${i}Wrapper`, "wrapper", "anotherClass");
  // setting html
  newDiv.innerHTML = `<div class="btn"id="${i}" onclick=alert("button!")>Button #${i}</div>`;
  // appending to parent (to append to page)
  container_div.appendChild(newDiv);
}
let button3counter = 0
let somethingHappened = function(){
  button3counter += 1
  alert(`Something happened! Clicked ${button3counter} times`)
}
let btn3 = document.getElementById('3')
btn3.addEventListener('click', somethingHappened)


// let allBtns = document.querySelectorAll('#btn');
// for (let i=0; i<allBtns.length; i++){
//   allBtns[i].onclick = function() {
//       alert(`button ${i}!`);
//   }
// }

// let btn1 = document.getElementById('1');
// console.log(btn1)
// btn1.style.display = 'none'
// btns = document.querySelectorAll('.btn')
// for (i in btns){
//     console.log(btns[i])
//     if (btns[i].hasAttribute('style')){       
//         console.log('found')
//         btns[i].style.display = ''
//     }
// }

// radio buttons
let btn6Wrapper = document.querySelector('.btn-6Wrapper')
let radioDiv = document.createElement("div")
radioDiv.innerHTML = `<input style="color: black" type="radio" name="fruit" value="Apples" checked> Apples<br>
                <input style="color: black" type="radio" name="fruit" value="Bananas"> Bananas<br>
                <input style="color: black" type="radio" name="fruit" value="Pears"> Pears`
btn6Wrapper.appendChild(radioDiv)

let fruitSelected = document.querySelector('input[name="fruit"]:checked').value
console.log('intial val', fruitSelected)

let btn4Wrapper = document.querySelector('.btn-4Wrapper')
let selectorDiv = document.createElement("div")
selectorDiv.innerHTML = `<select id="ddl">
                      <option value="volvo" selected>Volvo</option>
                      <option value="saab">Saab</option>
                      <option value="mercedes">Mercedes</option>
                      <option value="audi">Audi</option>
                      </select>`
btn4Wrapper.appendChild(selectorDiv)

let selectedCar = document.querySelector('#ddl')
let carEvent = function(){
  console.log(ddl.value)
}
selectedCar.addEventListener('change', carEvent)
console.log('initial val', ddl.value)

let btn7Wrapper = document.querySelector('.btn-7Wrapper')
let userInput = document.createElement("input")
userInput.type = "text"
btn7Wrapper.appendChild(userInput)
userInput.oninput = function(){
  console.log('user entered some text: ' + userInput.value)
}


let btn8Wrapper = document.querySelector('.btn-8Wrapper')
btn8Wrapper.onclick = function(event) {
  let x = event.clientX;
  let y = event.clientY;
  alert('position: '+x+', '+y);
}