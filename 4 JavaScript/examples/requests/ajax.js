let target = document.getElementById("target");
let textTarget = document.getElementById("textTarget")
let resultHTML = ''

let btn = document.getElementById('showQuote')
let setText = function(){
    let req = new XMLHttpRequest();
    req.addEventListener("progress", function(e) {
        console.log(e.loaded);
        target.innerText = "Loading...";
    });
    req.addEventListener("error", function(e) {
        console.log(e.status);
        target.innerText = "Cannot load quote. Try again later!";
    });
    req.addEventListener("load", function(e) {
        console.log(req.responseText);
        let response = JSON.parse(req.responseText);
        console.log(response);
        let resultHTML = `
            <p>${response.quote.body}</p>
            <p><i><a href="${response.quote.url}">${response.quote.author}</a></i></p>
            `
        textTarget.innerText = response.quote.body
    });
    req.open("GET", "https://favqs.com/api/qotd");
    req.setRequestHeader("Authorization", `Token token="${token}"`);
    req.send()
}

btn.addEventListener('click', setText)

