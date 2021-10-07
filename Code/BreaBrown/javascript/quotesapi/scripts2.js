// v2

// let page_id = 1
// let getData = function(){
//     let search = document.getElementById("search").value;
//     console.log(search);
//     axios.get(`https://favqs.com/api/quotes?&filter=${search}`, {
//             headers: { 
//                 Authorization: `Token token=${token}`
//                 }
//             }).then(response => {
//                 console.log(response);
                
//                     let data = response.data;
//                     let quotes = data.quotes;
//                     let target = document.getElementById("textTarget");
//                     for (i=0; i<quotes.length; i++){
//                             let quoteDiv = document.createElement('div')
//                             //quoteDiv.classList.add('container')
//                             quoteDiv.innerHTML = `<div>${quotes[i].body}</div><br>`
//                             target.appendChild(quoteDiv)
//                     }});
                    
// // ​}
        

let btn1 = document.getElementById('Search')
btn1.addEventListener('click', ()=>{console.log('btn')
let search = document.getElementById("search").value;
console.log(search);
axios.get(`https://favqs.com/api/quotes?&filter=${search}`, {
        headers: { 
            Authorization: `Token token=${token}`
            }
        }).then(response => {
            console.log(response);
            
                let data = response.data;
                let quotes = data.quotes;
                let target = document.getElementById("textTarget");
                for (i=0; i<quotes.length; i++){
                        let quoteDiv = document.createElement('div')
                        //quoteDiv.classList.add('container')
                        quoteDiv.innerHTML = `<div>${quotes[i].body}</div><br>`
                        target.appendChild(quoteDiv)
                }});
})



                    //let btn = document.getElementById('randomQuote')
// //btn.addEventListener('click', getData)