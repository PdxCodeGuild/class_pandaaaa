// M.AutoInit();
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
let app = new Vue({
  el: "#app",
  // change delimiters to avoid conflict with jinga
  delimiters: ["[[", "]]"],

  data: {
    message: "hello world",
    todos: [],
    todoName: "",
    todoDescription: "",
  },
  mounted: function () {
    // axios.get('{% url "list" %}')
    axios.get("get").then((response) => (app.todos = response.data.todos));
    // app.todos = response.data)
  },
  methods: {

    addTodo: function () {
    axios({
        method:'post',
        // url: 'http://localhost:8000/add/',
        url: 'add/',
        data: {
            name: this.todoName,
            description: this.todoDescription
        }
    }).then(function(){
    app.todos.push(
        {
            name: app.todoName,
            description: app.todoDescription,
            status: false
        }
    )  
      app.todoName = "";
      app.todoDescription = "";          
    })
    },
  },
});
