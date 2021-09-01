axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

var app = new Vue({
    el: '#app',
    data: {
        allStudents: [],
        modal: false
    },
    mounted: function() {
        axios.get('http://localhost:8000/api/')
        .then(function (response){
            app.allStudents = response.data;
        });
    },
    methods: {
        edit: function(id) {
        },
        remove_prompt: function(id,index){
            remove_student(id,index);
        },
        remove: function(id,index) {
            axios.delete('http://localhost:8000/api/' + id + '/')
            .then(function (response){
                app.allStudents.splice(index,1);
            });
        },
        add: function(){
            let new_student = add_student()
            // axios.post('http://localhost:8000/api/new/')
            // .then(function (response){
                // });
            },
        },
    });

let remove_student = function(id,index) {
    let student_name = document.querySelector('#student_name');
    let cancel_btn = document.querySelector('#close_prompt');
    let delete_btn = document.querySelector('#remove_student')
    student_name.innerText = app.allStudents[index].first_name + ' ' + app.allStudents[index].last_name;
    $("#remove-dialog").modal('show');
    cancel_btn.addEventListener('click', function(){
        $("#remove-dialog").modal('hide');
    })
    delete_btn.addEventListener('click',function(){
        $("#remove-dialog").modal('hide');
        app.remove(id,index);
    })
};

let add_student = function() {
    $("#create-dialog").modal('show')
    let first_name = document.querySelector('#fname')
    let last_name = document.querySelector('#lname')
    let cohort = document.querySelector('#cohort')
    let fav_topic = document.querySelector('#fav_topic')
    let fav_teacher = document.querySelector('#fav_teacher')
    let capstone = document.querySelector('#capstone')

    let cancel_btn = document.querySelector('#close_prompt');
    cancel_btn.addEventListener('click', function(){
        $("#remove-dialog").modal('hide');
    })
};

    