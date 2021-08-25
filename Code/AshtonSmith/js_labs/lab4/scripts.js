// class Date {
//     constructor(day, month, year) {
//         this.day = day;
//         this.month = month;
//         this.year = year;
//         this.months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
//     }

//     now() {
//         return this.day + " " + this.months[this.month - 1] + " " + this.year
//     }

// }

var app = new Vue({
    el: '#app',
    data: {
        formName: "",
        formDescription: "",
        formComplete: false,
        formDueDate: "",
        message: "",
        my_todos: [],
    },
    methods: {
        addTodo: function() {
            console.log("addTodo")
            let myForm = document.getElementById('myForm');
            let closeBtn = document.getElementById('closeBtn');
            // myContent.innerHTML = ""
            closeBtn.classList.remove('hide')
            myForm.classList.remove('hide')
        },
        submitTodo: function() {

            closeBtn.classList.add('hide')
            myForm.classList.add('hide')
        },
        populateTodo: function() {
            for (let i = 0; i < 25; ++i) {
                this.formName = i;
                this.formDescription = i;
                this.dueDate = "25-Aug-2021";
                this.my_todos.push({
                    "name": this.formName,
                    "dueDate": this.formDueDate,
                    "description": this.formDescription,
                    "isCompleted": false
                });
            }
        },
        markDone: function(index) {
            console.log("MARK DONE" + index + "...")
                // console.log(this.my_todos[index].isCompleted)
                // this.my_todos[index]["isCompleted"] = !this.my_todos[index]["isCompleted"]
            this.my_todos[index].isCompleted = !this.my_todos[index].isCompleted
        },
        listTodo: function() {
            let myForm = document.getElementById('myForm');
            // let myContent = document.getElementById('myContent')
            // myContent.innerHTML = ""
            myForm.classList.add('hide')
            closeBtn.classList.add('hide')
                // for (let i = 0; i < this.my_todos.length; ++i) {
                //     // var button = document.createElement("button");
                //     // button.onClick = app.addTodo
                //     // button.innerHTML = "New Button";
                //     myContent.innerHTML +=
                //         `<div class = "todoContainer"> ` +
                //         `<p class = "todoName">` + this.my_todos[i].name + `</p><br>` +
                //         `<p class = "todoDate">` + this.my_todos[i].dueDate + `</p><br>` +
                //         `<p class = "todoDescription">` + this.my_todos[i].description + `</p><br>` +
                //         // myContent.appendChild(button);
                //         // myContent.innerHtml +=
                //         `<button v-on:click="addTodo">List</button>` +
                //         `</div>`


            //     console.log(this.my_todos[i].name)
            // }
            console.log("HELLO?")
                // this.my_todos[i].dueDate
                // this.my_todos[i].description

        },

    }
})