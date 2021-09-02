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
      // axios to django views to save in database
      axios({
        method: "post",
        url: 'http://localhost:8000/todos/add/',
        data: {
          name: this.todoName,
          description: this.todoDescription,
        },
      }).then(function () {
        // only hands DOM
        app.todos.push({
          name: app.todoName,
          description: app.todoDescription,
          status: false,
        });
        app.todoName = "";
        app.todoDescription = "";
      });
    },
    removeTodo: function (todo_pk, index) {
      axios({
        method: "post",
        url: 'http://localhost:8000/todos/delete/',
        data: {
          pk: todo_pk,
        },
      }).then(function () {
        // only hands DOM
      app.todos.splice(index, 1);
      });

    },
  },
});
