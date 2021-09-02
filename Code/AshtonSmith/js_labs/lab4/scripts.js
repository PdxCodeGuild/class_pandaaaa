var app = new Vue({
        el: '#app',
        data: {
            formName: "",
            formDescription: "",
            formComplete: false,
            formDueDate: "",
            message: "",
            my_todos: [],
            currentIndex: 0,
        },
        methods: {
            addTodo: function() { //this function is used to display the form fields - to input a new todo.
                console.log("addTodo")
                let myForm = document.getElementById('myForm');
                let closeBtn = document.getElementById('closeBtn');
                let submitBtn = document.getElementById('submitBtn');
                let submitEdit = document.getElementById('editBtn');
                closeBtn.classList.remove('hide')
                myForm.classList.remove('hide')
                myForm.classList.add('flex')
                submitBtn.classList.remove('hide')
                submitEdit.classList.add('hide')
                this.formName = "";
                this.formDescription = "";
                this.formDueDate = "";
            },
            editTodo: function(index) {
                // this.my_todos[index]
                let submitBtn = document.getElementById('submitBtn');
                let myForm = document.getElementById('myForm');
                let closeBtn = document.getElementById('closeBtn');
                let submitEdit = document.getElementById('editBtn');
                submitEdit.classList.remove('hide')
                submitBtn.classList.add('hide')
                closeBtn.classList.remove('hide')
                myForm.classList.remove('hide')
                myForm.classList.add('flex')
                this.formName = this.my_todos[index].name;
                this.formDescription = this.my_todos[index].description;
                this.currentIndex = index;
                // this.formDueDate = this.my_todos[index].dueDate;

            },
            submitEdit: function() {
                // console.log(this.my_todos[index])
                this.my_todos[this.currentIndex].name = this.formName;
                this.my_todos[this.currentIndex].description = this.formDescription;
                this.my_todos[this.currentIndex].dueDate = this.formDueDate
                submitBtn.classList.remove('hide')
                closeBtn.classList.add('hide')
                myForm.classList.add('hide')
                myForm.classList.remove('flex')
                submitEdit.classList.add('hide')
            },
            submitTodo: function() {
                let submitBtn = document.getElementById('submitBtn');
                submitBtn.classList.add('hide')
                closeBtn.classList.add('hide')
                myForm.classList.add('hide')
                myForm.classList.remove('flex')
                this.my_todos.push({
                    "name": this.formName,
                    "dueDate": this.formDueDate,
                    "description": this.formDescription,
                    "isCompleted": false,
                });
            },
            populateTodo: function() {
                for (let i = 0; i < 25; ++i) {
                    this.formName = "Thing to do number " + i;
                    this.formDescription = "Gotta do this thing in building number " + i + ".";
                    this.formDueDate = "25-Aug-2021";
                    this.my_todos.push({
                        "name": this.formName,
                        "dueDate": this.formDueDate,
                        "description": this.formDescription,
                        "isCompleted": false,
                    });
                }
            },
            markDone: function(index) {
                console.log("MARK DONE" + index + "...")
                this.my_todos[index].isCompleted = !this.my_todos[index].isCompleted
            },
            listTodo: function() {
                let myForm = document.getElementById('myForm');
                myForm.classList.add('hide')
                myForm.classList.remove('flex')
                closeBtn.classList.add('hide')
            },
        }
    })
    // console.log(this.my_todos[index].isCompleted)
    // this.my_todos[index]["isCompleted"] = !this.my_todos[index]["isCompleted"]
    // // myContent.innerHTML = ""
    // // for (let i = 0; i < this.my_todos.length; ++i) {
    //     // let myContent = document.getElementById('myContent')
    //     //     // var button = document.createElement("button");
    //     //     // button.onClick = app.addTodo
    //     //     // button.innerHTML = "New Button";
    //     //     myContent.innerHTML +=
    //     //         `<div class = "todoContainer"> ` +
    //     //         `<p class = "todoName">` + this.my_todos[i].name + `</p><br>` +
    //     //         `<p class = "todoDate">` + this.my_todos[i].dueDate + `</p><br>` +
    //     //         `<p class = "todoDescription">` + this.my_todos[i].description + `</p><br>` +
    //     //         // myContent.appendChild(button);
    //     //         // myContent.innerHtml +=
    //     //         `<button v-on:click="addTodo">List</button>` +
    //     //         `</div>`


// //     console.log(this.my_todos[i].name)
// // }
// console.log("HELLO?")
//     // this.my_todos[i].dueDate
//     // this.my_todos[i].description
// myContent.innerHTML = ""
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