  // Installs globals onto window:
  // * Buffer
  // * require (monkey-patches if already defined)
  // * process
  // You can pass in an arbitrary object if you do not wish to pollute
  // the global namespace.
  BrowserFS.install(window);
  // Configures BrowserFS to use the LocalStorage file system.
  BrowserFS.configure({
    fs: "LocalStorage"
  }, function(e) {
    if (e) {
      // An error happened!
      throw e;
    }
    // Otherwise, BrowserFS is ready-to-use!
  });

var app = new Vue({
  el: "#app",
  data: {
    pageNum: 2,
    message: "HELLO",
    savedDogs: [],
    breedsList: [],
    age: 0,
    size: '',
    name: '',
    breed: '',
    dogPic: ''
  },
  mounted: function () {
    axios.get("https://dog.ceo/api/breeds/list/all").then(function (response) {
      console.log(response);
      let dogs = response.data.message;
      for (let [key, value] of Object.entries(dogs)){
          console.log(key)
          app.breedsList.push(key)
      }
    });
  },
  methods: {
      getPic: function(){
        axios
        .get(`https://dog.ceo/api/breed/${this.breed}/images/random`)
        .then(function (response) {
          app.dogPic = response.data.message;
          console.log(response.data.message);
        });
    },
    saveDog: function(){
        unsavedDog = {
            age: this.age,
            size: this.size,
            name: this.name,
            breed: this.breed,
            dogPic: this.dogPic           
        }
        this.savedDogs.push(unsavedDog)
        this.age = 0
        this.size =''
        this.name = ''
        this.breed = ''
        this.dogPic = ''
    },
    getPage: function(num){
        this.pageNum = num
    },
    saveAllDogs: function(){
        let data = JSON.stringify(this.savedDogs)
        var fs = require('fs');
        fs.writeFile('dogs.txt', 'Cool, I can do this in the browser!', function(err) {
          fs.readFile('dogs.txt', function(err, data) {
            console.log(data.toString());
          });
        });
    }
  }
});
