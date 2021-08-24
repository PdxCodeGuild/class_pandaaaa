// const axios = require('axios');

// const { default: axios } = require("axios");

// axios = 'axios'
let author = document.querySelector('#author');
let quote = document.querySelector('#quote');
let search_btn = document.querySelector('#search_btn');
let qotd_block = document.querySelector('#quote-block');
let search_block = document.querySelector('.search')
let url = 'https://favqs.com/api/qotd';

axios.get(url)
    .then(function (response){
        author.innerText = response.data.quote.author;
        quote.innerText = response.data.quote.body;
    })
    .catch(function (error){
        console.log(error);
    });

search_btn.addEventListener('click',function() {
    search_field = document.querySelector('#search').value;
    // console.log(search_field)
    axios.get('https://favqs.com/api/quotes',{
        headers: {
            Authorization: 'Token token=686401e5319a53cd665f3bddf59c6714',
        },
        params: {
            page : 1,
            filter : search_field,
        }
    })
        // This line is important or else it breaks?
        .catch(function (error){
            console.log(error)
        })
        .then(function (response){
            let quotes = response.data.quotes;
            // console.log(quotes)
            let n = response.data.quotes.length
            for (let i = 0; i < n; ++i) {
                // Oh sanjeet
                // if (quotes[i].body == quotes[0].body && i != 0){
                //     break;
                // }
                let quote_block = document.createElement('div');
                let quote_html = `<div class="card">
                <div class="card-header">
                    Quote
                </div>
                <div class="card-body" id='quote-block'>
                    <blockquote class="blockquote mb-0">
                    <p><span id="quote">${quotes[i].body}</span></p>
                    <footer class="blockquote-footer"><span id="author">${quotes[i].author}</span></footer>
                    </blockquote>
                </div>
            </div>
    `
                // author.innerText = quotes[i].author;
                quote_block.innerHTML = quote_html
                search_block.append(quote_block)
                // document.body.insertBefore(quote_block, qotd_block)
            }
        });
});
