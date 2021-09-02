let app = new Vue({
  el: "#app",
  data: {
    breedsList: [],
    dogsList: [],
    dogName: "",
    dogBreed: "",
    dogPic: "",
    pageNum:1,
  },
  mounted: function () {
    axios.get("https://dog.ceo/api/breeds/list/all").then(function (response) {
      console.log(response.data.message);
      let dogs = response.data.message;
      for (const [key, value] of Object.entries(dogs)) {
        // console.log(`${key}: ${value}`);
        app.breedsList.push(key);
      }
    });
  },
  methods: {
    getPic: function () {
      axios
        .get(`https://dog.ceo/api/breed/${this.dogBreed}/images/random`)
        .then(function (response) {
          app.dogPic = response.data.message;
          console.log(response.data.message);
        });
    },
    saveDog: function () {
      newDog = {
        name: this.dogName,
        breed: this.dogBreed,
        pic: this.dogPic,
      };
      this.dogsList.push(newDog);
      this.dogName = "";
      this.dogBreed = "";
      this.dogPic = "";
    },
    getPage: function(num){
        this.pageNum = num
    }
  },
});
