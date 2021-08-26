var app = new Vue({
  el: "#app",
  data: {
    pageNum: 2, // number to navigate state of "pages"
    savedDogs: [],
    breedsList: [],
    age: 0,
    size: "",
    name: "",
    breed: "",
    dogPic: "",
  },
  mounted: function () {
    // get all dog breeds from api to populate form select
    axios.get("https://dog.ceo/api/breeds/list/all").then(function (response) {
      console.log(response);
      let dogs = response.data.message;
      for (let [key, value] of Object.entries(dogs)) {
        console.log(key);
        app.breedsList.push(key);
      }
    // to load dogs from local file: 
    // because of CORS error, must run on server: npm install --global http-server
    // then: run http-server in project directory
    axios.get('mydogs.json')
    .then(function(response){
      console.log(response)
      app.savedDogs= response.data
    })
    // to load dogs from local storage:
    app.savedDogs = JSON.parse(window.localStorage.getItem("savedDogs"))
    });
  },
  methods: {
    // get random picture from api
    getPic: function () {
      axios
        .get(`https://dog.ceo/api/breed/${this.breed}/images/random`)
        .then(function (response) {
          app.dogPic = response.data.message;
          console.log(response.data.message);
        });
    },
    // save dog to list in root
    saveDog: function () {
      unsavedDog = {
        age: this.age,
        size: this.size,
        name: this.name,
        breed: this.breed,
        dogPic: this.dogPic,
      };
      this.savedDogs.push(unsavedDog);
      this.age = 0;
      this.size = "";
      this.name = "";
      this.breed = "";
      this.dogPic = "";
    },
    // change "page"
    getPage: function (num) {
      this.pageNum = num;
    },
    // save dogs to local storage: load them on mounted
    saveAllDogs: function () {
      const data = JSON.stringify(this.savedDogs);
      window.localStorage.setItem("savedDogs", data);
      console.log(JSON.parse(window.localStorage.getItem("savedDogs")));
    },
    // save dogs in "Blob" to download from browser
    downloadDogs:function() {
      const data = JSON.stringify(this.savedDogs)
      const blob = new Blob([data], {type: 'text/plain'})
      const e = document.createEvent('MouseEvents'),
      a = document.createElement('a');
      a.download = "test.json";
      a.href = window.URL.createObjectURL(blob);
      a.dataset.downloadurl = ['text/json', a.download, a.href].join(':');
      e.initEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
      a.dispatchEvent(e);
  }
  },
});
