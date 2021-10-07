axios.get("https://favqs.com/api/qotd")
.then(function(response){
    author = document.getElementById("author")
    keyword = document.getElementById("keyword")
    tag = document.getElementById("tag")
    author.innerText = response.data.quote.author
})