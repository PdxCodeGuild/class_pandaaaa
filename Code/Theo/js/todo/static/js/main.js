import axios from 'axios';
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.xsrfCookieName = 'csrftoken';

let app = new Vue({
    el: '#app',
    delimiters: ["[[","]]"],
    data: {
        tasks: [],
        text: '',
        created_date: '',
        completed_date: '',
        completed: false,
    },
    mounted:
        function(){
            axios.get('get')
            .then(function (response){
                app.tasks = response.data.data;
                console.log(response.data);
            })
    },
    methods: {
        addTask: function() {
            axios({
                method:'post',
                url: '',
                data: {
                    text: this.text,
                }
            })
            this.text = "";
        }
    }
})