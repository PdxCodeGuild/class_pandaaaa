// let yoName = prompt('whats yo name?')
// alert('hello ' + yoName)
// alert(`template literal ${ yoName }`)
// document.write('<span>Hello World!</span>')

// let texts = 'A backslash followed by a \
// newline in a string literal will continue \
// that string. The resulting string won\
// t contain a backslash or a newline.'
 
// let fruits = [ 'apples', 'banan', 'pear', 'kiwi' ]

// let favFruit = printstuff_named(fruits)
// console.log('my fav fruit is ', favFruit)

// // will run because printstuff is brought to top on load
// console.log(printstuff_anon(fruits))
// // Uncaught ReferenceError: Cannot access 'printstuff_anon' before initialization
// console.log(printstuff_named(fruits))

// // named function
// function printstuff_named(list) {
//     console.log(list);
//     console.log(list)
//     let chosenFruit = list[Math.floor(Math.random()*list.length)];
//     return chosenFruit
// }
// // anonymous Function
// let printstuff_anon = function(list) {
//     console.log(list)
//     let chosenFruit = list[Math.floor(Math.random()*list.length)];
//     return chosenFruit
// }



// let x = 7; 

// // ternary if
// (x == 7)? console.log('true') : console.log('false');

// if (x==7){
//     console.log('true')
// } 
// else if (x==8) {
//     console.log('x = 8')
// }
// else if (x==8) {
//     console.log('x = 8')
// }
// else if (x==9) {
//     console.log('x = 9')
// }
// else{
//     console.log('whatever')
// }


// x = '5';
// y = 5;

// if (x==y){
//     console.log('true')
// }
// console.log()


let btn = document.querySelector('#btn')

// button.onclick = function() {
//     let name_input = document.querySelector('#name_input')
//     let name_value = name_input.value
//     alert(name_value)
// }


btn.addEventListener('click', function() {
    alert('clicked!')
})

let action = () => alert('clicked!');
btn.addEventListener('click', action);


// let invalidInput = true;
// while (invalidInput) {
//     answer = prompt("Pick a number from one to ten");
//     if (answer >= 1 && answer <= 10) {
//         invalidInput = false;
//     }
// }