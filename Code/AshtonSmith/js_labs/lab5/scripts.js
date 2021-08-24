// let url = "https://favqs.com/api/qotd"
let url = "https://favqs.com/api/quotes/?filter="
let target = document.getElementById("target");
let textTarget = document.getElementById("textTarget")
let searchTerm = document.getElementById("search")
let currPage = 1
let myLoading = document.getElementById("loadingBar")

let getData = function() {
    console.log(url + searchTerm.value)
    myLoading.classList.remove("hide")
    let myUrl = url + searchTerm.value + "&page=" + currPage
    axios.get(myUrl, {
        headers: {
            Authorization: `Token token="${token}"`,
        }
    }).then(response => {
        target.innerHTML = ""
            // target = document.createElement('div')
            // target.setAttribute("id", "target")
        console.log(response.data)
        for (let i = 0; i < response.data.quotes.length; ++i) {
            let quoteDiv = document.createElement('div')
            let authorDiv = document.createElement('div')
            quoteDiv.innerText = response.data.quotes[i].body
            authorDiv.innerText = "-" + response.data.quotes[i].author
            authorDiv.classList.add('quoteAuthor');
            quoteDiv.classList.add('quoteBody');
            quoteDiv.appendChild(authorDiv)
            target.appendChild(quoteDiv)
        }
        //determine pagination button requirements.. then add or remove buttons.
        currPageBtn.innerText = "PAGE: " + currPage;
        if (!response.data.last_page) {
            if (currPage != 1)
                prePageBtn.classList.remove('hide')
            else
                prePageBtn.classList.add('hide')
            nextPageBtn.classList.remove('hide')
        } else {
            nextPageBtn.classList.add('hide')
        }
    }).finally(() => {
        myLoading.classList.add("hide")
        console.log("finally")
    })
}

function nextPage() {
    ++currPage;
    console.log("PAGE: " + currPage)
    getData();
}

function prePage() {
    --currPage;
    console.log("PAGE: " + currPage)
    getData();
}

function searchData() {
    currPage = 1;
    console.log("PAGE: " + currPage)
    getData();
}

let btn = document.getElementById('showQuote')
let nextPageBtn = document.getElementById('nextPageBtn')
let currPageBtn = document.getElementById('currPage')
let prePageBtn = document.getElementById('prePageBtn')

let setText = function() {
    textTarget.innerHTML = resultHTML;
    console.log(resultHTML)
    console.log(textTarget)
}

btn.addEventListener('click', searchData)
nextPageBtn.addEventListener('click', nextPage)
prePageBtn.addEventListener('click', prePage)