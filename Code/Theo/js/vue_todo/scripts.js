let app = new Vue({
    el: '#app',
    data: {
        tasks: [],
        name: '',
        completed: false,
    },
    methods: {
        addTask: function() {
            let task = {
                name: this.name,
                completed: this.completed
            }
            this.tasks.push(task);
            this.name = '';
        },
        removeTask: function(index) {
            this.tasks.splice(index,1);
        }
    }
})