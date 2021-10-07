let app = new Vue({
    el: '#app',
    // change delimiters to avoid conflict w jinga
    delimiters: ["[[","]]"],
    data: {
        message: 'hello world',
        todos: [],
        todoName : '',
        todoDescription: '',
    },
    mounted : {
        function(){
            axios.get()('{% url "todo_list_app:index" %}')
            .then((response) => 
            app.todos = response.data.todos)
            }
    },
    methods : {
        addTodo : function(){
            console.log('add: ', app.todoName);

            app.todoName = "";
            app.todoDescription = "";
        }, 
    },

});