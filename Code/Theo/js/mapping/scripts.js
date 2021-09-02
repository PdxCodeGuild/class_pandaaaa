class User {
    constructor(name,lat,lon) {
        this.name = name;
        this.lat = lat;
        this.lon = lon;
    }
};

let app = new Vue({
    el: '#app',
    data: {
        users : [],
        url : 'https://jsonplaceholder.typicode.com/users',
    },
    mounted: function() {
        // console.log('Hello there')
        let map = L.map('mapid').setView([51.505, -0.09], 2);

        L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
            maxZoom: 18,
            id: 'mapbox/streets-v11',
            tileSize: 512,
            zoomOffset: -1,
            accessToken: 'pk.eyJ1IjoidHJvd2xldHQiLCJhIjoiY2tzcWtha3k0MGNzYzJ3bzNqcGxjNXBxcCJ9.aRuVzA3myC5mEiobS_eZ5w'
        }).addTo(map);

        axios.get('https://jsonplaceholder.typicode.com/users')
        .then(function (response){
            for (let i = 0; i < response.data.length; ++i){
                let name = response.data[i].name;    
                let lat = response.data[i].address.geo.lat;    
                let lon = response.data[i].address.geo.lng;
                app.users.push(new User(name,lat,lon));    
                let marker = L.marker([lat,lon]).addTo(map);
                marker.bindPopup(name).openPopup();
            }
        });
    },
});