//Zach Watts
//Lab 
//ModCode Vue

let app = new Vue({
    el: '#app',
    data: {
        message: 'Hello',
        //list for user info
        users: []
    },
    mounted:function(){
        var mymap = L.map("mapid").setView([51.505, -0.09], 3);
        L.tileLayer(
          "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
          {
            attribution:
              'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
            maxZoom: 18,
            id: "mapbox/streets-v11",
            tileSize: 512,
            zoomOffset: -1,
            accessToken:
              `${token}`,
          }
        ).addTo(mymap);
    },
    methods: {
        getUsers: function(){
            console.log('hello')
            axios.get("https://jsonplaceholder.typicode.com/users")
            .then(function(response){
                console.log(response)
                for(let i in response.data){
                    let personData = response.data[i]
                    let person = {
                        'name':personData.name,
                        'lat':personData.address.geo.lat,
                        'long': personData.address.geo.lng
                    };
                    // push person to list
                    app.users.push(person)
                }
                
            }).catch(function(error){console.log(error)})
        },
        newMessage: function(){
            this.message= 'Donnie you"re out of your element'
        },
        addUser: function(){
            let newUser = {
                'name': this.name,
                'lat': this.lat,
                'long': this.long
            }
            this.users.push(newUser)
            this.name = ''
            this.lat = 0
            this.long = 0
        }
    }
},)
// button = documentgetElementById('id')
// button.addEventListener('click', function)