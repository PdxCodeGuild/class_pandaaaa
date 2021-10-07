let app = new Vue({
    el: '#app',
    data: {
        newToDo: '',
        todos: [],
    },

    methods: {
        add: function() {
          this.todos.push({
            id: this.todos.length + 1,
            name: this.newToDo,
            completed: false,
            edit: false,
          });
          this.newToDo = '';
        },
        remove: function(index) {
          this.todos.splice(index, 1);
        }
      },
})