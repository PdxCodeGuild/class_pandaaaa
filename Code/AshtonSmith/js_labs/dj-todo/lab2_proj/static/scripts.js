// import axios from 'axios';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
// console.log("js")


var app = new Vue({
    el: '#app',
    delimiters: ["[[", "]]"],
    data: {
        name: " test",
        details: " test",
        priority: "high",
        starttime: "12:30",
        startdate: "2021-09-30",
        completed: false,
        todos: []
    },
    mounted: function() {
        axios.get("get").then((response) =>
            app.todos = response.data.todos)
    },
    methods: {

        addTodo: function() {
            let my_data = {
                name: this.name,
                details: this.details,
                priority: this.priority,
                starttime: this.starttime,
                startdate: this.startdate,
            }
            this.todos.push(my_data)
            axios({
                method: "post",
                url: "add",
                // headers: {
                //     'X-CSRFToken': '{{csrf_token}}'
                // },
                data: my_data,

            })
        },
    }
})