axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

var app = new Vue({
  el: "#app",
  data: {
    first_name: "",
    last_name: "",
    fav_teacher: "",
    cohort: "",
    currentStudentPK: "",
    allStudents: [],
    editing: false,
    adding: false,
    //   currentRoute: window.location.pathname
  },
  mounted: function () {
    axios.get("http://localhost:8000/apis/v1/").then(function (response) {
      app.allStudents = response.data;
    });
  },
  // watch: {
  //   // whenever allStudents changes, this function will run
  //   allStudents: function () {
  //     axios.get("http://localhost:8000/apis/v1/").then(function (response) {
  //       app.allStudents = response.data;
  //     });    
  //   }
  // },
  methods: {
    getStudents: function () {
      axios.get("http://localhost:8000/apis/v1/").then(function (response) {
        app.allStudents = response.data;
      });
    },
    studentDetail: function (pk) {
      this.currentStudentPK = pk;
    },
    updateStudent: function (pk) {
      this.editing = false;
      axios({
        method: "put",
        url: "http://localhost:8000/apis/v1/" + pk + "/",
        data: {
          first_name: this.first_name,
          last_name: this.last_name,
          favorite_teacher: this.fav_teacher,
          cohort: this.cohort,
        },
      }).then(function (response) {
        this.first_name = "";
        this.last_name = "";
        this.fav_teacher = "";
        this.cohort = "";
        app.getStudents()
      });
    },
    addStudent: function () {
      axios({
        method: "post",
        url: "http://localhost:8000/apis/v1/",
        data: {
          first_name: this.first_name,
          last_name: this.last_name,
          favorite_teacher: this.fav_teacher,
          cohort: this.cohort,
        },
      }).then(function (response) {
        this.first_name = "";
        this.last_name = "";
        this.fav_teacher = "";
        this.cohort = "";
        app.getStudents()
      });
    },
    deleteStudent: function (pk) {
      this.currentStudentPK = "";
      axios({
        method: "delete",
        url: "http://localhost:8000/apis/v1/" + pk + "/",
        data: {
          pk: pk,
        },
      }).then(function () {app.getStudents()
      });
    },
  },
});

// let response = axios.get("http://localhost:8000/apis/v1/", {headers: {"X-CSRFTOKEN":"csrftoken"}})
// .then(function(response){ console.log(response)})
