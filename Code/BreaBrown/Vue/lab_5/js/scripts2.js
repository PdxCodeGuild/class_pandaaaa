let app = new Vue({
    el: '#app',
    data: {
        search: '',
        qotd: '',
        qotdAuthor: '',
        results : [],

    },

    mounted: 
        function(){
            axios.get("https://favqs.com/api/qotd")
            .then(function(response){
            console.log(response)
            app.qotd = response.data.quote.body
            app.qotdAuthor = response.data.quote.author        
            })
        },
    methods: {
        searchQuotes: function(){
            axios.get(`https://favqs.com/api/quotes?&filter=${this.search}`, {
        headers: { 
            Authorization: `Token token="${token}"`
            }
        }).then(response => {
            console.log(response);
            quotes = reponse.data.quotes;
            

        }).catch(error=>{
            console.log(error);
        });
    }
        }
    })