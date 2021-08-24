let target = document.getElementById("target");
let textTarget = document.getElementById("textTarget");
let loading = document.getElementById("loading");


let getData = function () {
  loading.innerHTML =
    '<div class="lds-spinner"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>';
  
  
    let searchinput = document.getElementById("search").value;
  let searchTerm = searchinput;
  console.log(searchTerm);
  axios
    .get(`https://favqs.com/api/quotes?page="+page_id+"&filter=${searchTerm}`, {
      headers: {
        Authorization: `Token token="${token}"`,

      },
    })
    .then(function(response){
      console.log(response)
      data = response.data.quotes;
      console.log(data);
      // for (let i = 0; i < data.length; i++) {
        data.forEach(element => {
        // console.log(i);
        // quote = `<div class="item"> <p class="quote">${data[i].body}</p> <p class="author">${data[i].author}</p></div>`;
        quote = `<div class="item"> <p class="quote">${element.body}</p> <p class="author">${element.author}</p></div>`;
        
        newDiv1 = document.createElement("div");
        newDiv1.innerHTML = quote;
        quoteContainer = document.getElementById("textTarget");
        quoteContainer.appendChild(newDiv1);
        }
    
    )})
    .catch(function(error){
        console.log(error)
    })
    .finally(() => {
      loading.innerHTML = "";
    });
};
let btn = document.getElementById("searchBtn");
// let setText = function(){
//     textTarget.innerHTML = resultHTML;
//     console.log(resultHTML)
//     console.log(textTarget)
// }
btn.addEventListener("click", getData);
