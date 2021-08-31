axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

var app = new Vue({
    el: "#app",
    data: {
      currentStudentPK: '',
      allStudents: [],
      editing: false,
      adding: false
    //   currentRoute: window.location.pathname
    },
    mounted: function () {
      axios.get("http://localhost:8000/apis/v1/").then(function (response) {
        app.allStudents = response.data;
      });
    },
    methods: {
      studentDetail: function(pk){
        this.currentStudentPK = pk
      },
      updateStudent: function(pk){
        this.editing = false
      },
      deleteStudent: function(pk){
        this.currentStudentPK = ''
      }
    }
  });

// let response = axios.get("http://localhost:8000/apis/v1/", {headers: {"X-CSRFTOKEN":"csrftoken"}})
// .then(function(response){ console.log(response)})