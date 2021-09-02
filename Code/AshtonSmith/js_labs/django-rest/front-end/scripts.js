axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

var app = new Vue({
    el: '#app',
    delimiters: ["[[", "]]"],
    data: {
        message: "message in vue",
        currentStudents: [],
        searchBy: ""
    },
    mounted: function() {
        // let url = "http://127.0.0.1:8000/apis/v1/"
        let url = "http://127.0.0.1:8000/apis/v1/search/custom/?search=" + this.searchBy
        axios.get(url).then((response) => {
            console.log(response.data)
            for (let i = 0; i < response.data.length; ++i) {
                this.currentStudents.push(response.data[i])
            }
            console.log(this.currentStudents)
        })
    },
    methods: {
        searchName: function() {
            this.currentStudents = []
            let url = "http://127.0.0.1:8000/apis/v1/search/custom/?search=" + this.searchBy
            axios.get(url).then((response) => {
                console.log(response.data)
                for (let i = 0; i < response.data.length; ++i) {
                    this.currentStudents.push(response.data[i])
                }
                console.log(this.currentStudents)
            })
            return 0
        }
    }
})