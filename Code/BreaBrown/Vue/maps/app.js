let app = new Vue({
    el: '#app',
    data: {
        message: 'Hello',
        // list for user profile
        users: [],
    },
    mounted: function(){
        console.log('in function')
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
              "pk.eyJ1Ijoic2J0cmllcyIsImEiOiJja3NveXNmeTgwMHE2MnJvMGo5cWw5YW84In0.q9_oeyCTuKZ8azNXe-XHvA",
          }
        ).addTo(mymap);   
    },
    
    methods: {
        getUsers: function(){
            console.log('clicked')
            // get data from endpoint
            axios.get("https://jsonplaceholder.typicode.com/users")
            .then(function(response){
                console.log(response)
                for (let i in response.data){
                    let personData = response.data[i];
                    let person = {
                        'name': personData.name,
                        'lat': personData.address.geo.lat,
                        'long': personData.address.geo.lng
                    };
                    // push person to list
                    app.users.push(person)
                }
            })
        },
        newMessage: function(){
            this.message = 'new stupid messsage'
        }
    }
})