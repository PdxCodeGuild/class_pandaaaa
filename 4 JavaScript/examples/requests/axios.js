let target = document.getElementById("target");
let textTarget = document.getElementById("textTarget")

let getData = function(){ 
axios.get('https://favqs.com/api/qotd', {
    headers: { 
    Authorization: `Token token="${token}"`
    }
}).then(response => {
console.log(response.data)
    let data = response.data
    let quote = data.quote
    let quoteDiv = document.createElement('div')
    quoteDiv.innerText = quote.body
    target.appendChild(quoteDiv)
})
}
let searchinput= document.getElementById('search')
let btn = document.getElementById('search')
// let setText = function(){
//     textTarget.innerHTML = resultHTML;
//     console.log(resultHTML)
//     console.log(textTarget)
// }
btn.addEventListener('click', getData)

