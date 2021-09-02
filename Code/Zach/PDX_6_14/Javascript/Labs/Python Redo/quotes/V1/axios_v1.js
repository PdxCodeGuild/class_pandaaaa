//Zach Watts
//Lab 9
//Random Quote Pull

//Version #1

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

let btn = document.getElementById('randomQuote')
btn.addEventListener('click', getData)