let app = new Vue({
    el: '#app',
    data: {
        author: '',
        quote: '',
        search: '',
        quotes: []
    },
    mounted: function() {
        axios.get('https://favqs.com/api/qotd')
            .then(function (response){
                app.quotes.push({
                    quote: response.data.quote.body,
                    author: response.data.quote.author
                })
            })
            .catch(function (error){
                console.log(error);
            });
    },
    methods: {
        getQuotes: function() {
            axios.get('https://favqs.com/api/quotes',{
                headers: {
                    Authorization: 'Token token=686401e5319a53cd665f3bddf59c6714',
                },
                params: {
                    page : 1,
                    filter : this.search,
                }
            })
                .catch(function (error){
                    console.log(error)
                })
                .then(function (response){
                    let n = response.data.quotes.length
                    app.quotes = []
                    for (let i = 0; i < n; ++i) {
                        let a_quote = {
                            quote: response.data.quotes[i].body,
                            author: response.data.quotes[i].author,
                            id: response.data.quotes[i].id
                        };
                        app.quotes.push(a_quote)
                    }
                }) 
        }
    }
});
 