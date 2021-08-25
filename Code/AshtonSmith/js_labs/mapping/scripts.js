// var circle = L.circle([51.508, -0.11], {
//     color: 'red',
//     fillColor: '#f03',
//     fillOpacity: 0.5,
//     radius: 500
// }).addTo(mymap);

// var polygon = L.polygon([
//     [51.509, -0.08],
//     [51.503, -0.06],
//     [51.51, -0.047]
// ]).addTo(mymap);

// marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();
// circle.bindPopup("I am a circle.");
// polygon.bindPopup("I am a polygon.");

// var popup = L.popup()
//     .setLatLng([51.5, -0.09])
//     .setContent("I am a standalone popup.")
//     .openOn(mymap);




var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue!',
        users: [],
        mymap: L.map('mapid').setView([0, 0], 3),
        lat: 0.0,
        long: 0.0,
        name: "",
    },
    methods: {
        getUsers: function() {
            axios.get("https://jsonplaceholder.typicode.com/users/")
                .then(function(response) {
                    for (let i in response.data) {
                        let personData = response.data[i];
                        let person = {
                            'name ': personData.name,
                            'lat': personData.address.geo.lat,
                            'long': personData.address.geo.lng
                        };
                        app.users.push(person)
                    }

                    // console.log("HEREEEEEEEEEEEEEEEEEEEEEEEEEEE");
                    // console.log(app.users)
                })
        },
        getMap: function() {
            L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
                attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
                maxZoom: 18,
                id: 'mapbox/streets-v11',
                tileSize: 512,
                zoomOffset: -1,
                accessToken: 'pk.eyJ1IjoiYXNodG9uMjMiLCJhIjoiY2tzcWpudGcyMGQ5OTJ2cG95ZW5tMmdndSJ9.v1Ey2HxUKmx0T6xk05YNKw'
            }).addTo(this.mymap);

            app.mymap.on('click', onMapClick);



            var popup = L.popup();



            this.mymap.on('click', onMapClick);
            users = [];
            fetch('https://jsonplaceholder.typicode.com/users/')
                .then(response => response.json())
                .then(json => {
                    for (let i = 0; i < json.length; ++i) {
                        users.push(json[i])
                            // user[i] = json[i]
                    }
                }).then(() => {
                    // console.log(users)
                    // console.log(users.length)
                    for (let i = 0; i < 10; ++i) {
                        // console.log("...............")
                        // console.log("wot" + users[i].address.geo.lat)
                        let currentMarker = L.marker([users[i].address.geo.lat, users[i].address.geo.lng])
                        currentMarker.bindPopup("<b>" + users[i].name + "</b><br>" + users[i].address.street + ", " + users[i].address.suite + "<br>" + users[i].address.city)
                        currentMarker.addTo(this.mymap);
                    }
                })

            function onMapClick(e) {
                popup
                    .setLatLng(e.latlng)
                    .setContent("You clicked the map at " + e.latlng.toString())
                    .openOn(this.mymap);
            }
        },
        onMapClick: function(e) {
            alert("You clicked the map at " + e.latlng);
        },
        addUser: function() {
            let person = {
                'name': this.name,
                'lat': this.lat,
                'long': this.long
            };
            app.users.push(person)
                // console.log("HEREEEEEEEEEEEEEEEEEEEEEEEEE")
                // console.log(app.users[app.users.length - 1].name)
                // console.log(app.users[app.users.length - 1].lat)
                // console.log(app.users[app.users.length - 1].long)
            let currentMarker = L.marker([app.users[app.users.length - 1].lat, app.users[app.users.length - 1].long])
            currentMarker.bindPopup("<b>" + app.users[app.users.length - 1].name + "</b><br>")
            currentMarker.addTo(this.mymap)

        }
    }
})