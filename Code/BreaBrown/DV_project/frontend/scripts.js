axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

var app = new Vue({
    el: '#app',
    delimiters:["[[","]]"],
    data:{
        mystudents: [],
    },
    mounted: function(){
        let url = 'http://localhost:8000/api/v1'
        axios.get(url).then(response => {
            console.log(response.data)
            for (let i = 0; i < response.data.length; i++){
                this.mystudents.push(response.data[i])
            }
        })
    },
})
