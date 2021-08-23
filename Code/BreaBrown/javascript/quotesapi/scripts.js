axios.get("https://favqs.com/api/qotd")
.then(function(response){
    author = document.getElementById("author")
    quote = document.getElementById("quote")
    console.log(quote)
    console.log(response)
    quote.innerText = response.data.quote.body
    author.innerText = response.data.quote.author
})


