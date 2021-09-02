//Zach Watts
//Lab 4
//VueTodo

let app = new Vue({
    el: '#app',
    data: {
        task: '',
        priority:'',
        message: 'Hello',
        //list for user info
        todos: []
    },
    methods: {
        // getTasks: function(){
        //     console.log('hello')
        //     for(let i in todos){
        //         let task =
        //     }
    //     }
    // }

    // },
        addTodo: function(){
            let newTodo = {
                'task': this.task,
                'priority': this.priority,
            }
            this.message = "some new string"
            this.todos.push(newTodo)
            this.task = ''
            this.priority = ''
        }
    }
})
