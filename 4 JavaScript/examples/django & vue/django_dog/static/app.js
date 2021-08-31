var app = new Vue({
    el: "#app",
    delimiters: ["[[", "]]"],

    data: {
      savedDogs: [],
      breedsList: [],
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
  });