let app = new Vue({
    el: '#app',
    data: {
        message: 'hello',
    },
    watch: {
        message: function(){
            alert('message has changed')
        }
    },
    computed: {
        reversedMessage: function () {
            // `this` points to the vm instance
            return this.message.split('').reverse().join('')
          }
    },
    // LIFECYCLE HOOKS: 
    // (more here:  )
    beforeCreate:{
        // Called synchronously after the instance has just been initialized, 
        // before data observation and event/watcher setup.
    },
    created: function(){
        // Called synchronously after the instance is created. 
        // At this stage, the instance has finished processing the options 
        // which means the following have been set up: data observation, computed properties, methods, watch/event callbacks. However, the mounting phase has not been started, and the $el property will not be available yet. 
    },
    beforeMount: function(){
        // Called right before the mounting begins: 
        // the render function is about to be called for the first time.
    },
    mounted: function(){
        // Called after the instance has just been mounted where el 
        // is replaced by the newly created vm.$el. 
    },
    beforeUpdate: function(){
        // Called when the data changes, 
        // before the virtual DOM is re-rendered and patched.
    },
    updated: function(){
        // Called after a data change causes the
        //  virtual DOM to be re-rendered and patched.
    },
    methods: {
        methodName: function(){
            this.message = 'you clicked the button'
        },
        populateMap: function(){
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

            let url = "https://jsonplaceholder.typicode.com/users";

            axios.get(url).then(function (response) {
                // handle success
                let personList = [];
                for (let person in response.data) {
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
                      `;
                  // jquery
                  $("#usercard").append(newCard);
                  //  or do:
                  //     usercard = document.getElementById('usercard');
                  //     usercard.append(newCard)
                }
              });
        }


    }
})