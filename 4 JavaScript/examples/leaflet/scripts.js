var mymap = L.map('mapid').setView([51.505, -0.09], 3);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1Ijoic2J0cmllcyIsImEiOiJja3NveXNmeTgwMHE2MnJvMGo5cWw5YW84In0.q9_oeyCTuKZ8azNXe-XHvA'
}).addTo(mymap);

let url = 'https://jsonplaceholder.typicode.com/users'

axios.get(url)
.then(function (response) {
    // handle success
    let personList = [];
    for (let person in response.data){ 
        let userInfo = response.data[person];
        console.log(userInfo);
        let lat = userInfo.address.geo.lat;
        let long = userInfo.address.geo.lng;
        let marker = L.marker([lat, long]).addTo(mymap);
        marker.bindPopup(`${userInfo.name} <p> ${lat}, ${long}</p>`).openPopup();
        // create new card for each user
        let newCard = `
            <div class="card">
                <div class="card-body">
                <h5 class="card-title">${userInfo.name}</h5>
                <li id="location">lat: ${userInfo.address.geo.lat} long: ${userInfo.address.geo.lng}</li>
                <li id="location"> ${userInfo.address.city}</li>
                </div>
            </div> 
        `
        // jquery
         $('#usercard').append(newCard);
        //  or do: 
        //     usercard = document.getElementById('usercard');
        //     usercard.append(newCard)
    };
});