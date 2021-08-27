var app = new Vue({
    el: '#app',
    data: {
        message: "message in vue",
        searchTerm: "horse",
        currPage: 1,
        currentQuotes: []
    },
    methods: {
        requestApi: function() {
            let url = "https://favqs.com/api/quotes/?filter=" + this.searchTerm + "&page=" + this.currPage
            console.log(url)
            console.log(token)
            axios.get(url, {
                headers: { Authorization: `Token token="${token}"` }
            }).then(response => {
                // console.log(response.data.last_page)
                let preBtn = document.getElementById("preBtn")
                let nextBtn = document.getElementById("nextBtn")
                let currPageBtn = document.getElementById("currPageBtn")
                currPageBtn.classList.add('hide')
                if (this.currPage > 1)
                    preBtn.classList.remove('hide');
                else
                    preBtn.classList.add('hide');

                if (response.data.last_page)
                    nextBtn.classList.add('hide');
                else
                    nextBtn.classList.remove('hide');

                this.currentQuotes = []
                for (let i = 0; i < response.data.quotes.length; ++i) {
                    this.currentQuotes.push(response.data.quotes[i]);
                }
                if (this.currentQuotes != [])
                    currPageBtn.classList.remove('hide')
            })

            // for (let i = 0; i < reponse.length; ++i) {}
            // data.quotes
        },
        nextPage: function() {
            ++this.currPage;
            this.requestApi()
        },
        prePage: function() {
            --this.currPage;
            this.requestApi()
        },
        newSearch: function() {
            this.currPage = 1;
            this.requestApi()
        }
    }
})