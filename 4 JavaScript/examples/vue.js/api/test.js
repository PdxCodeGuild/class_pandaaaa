let app = new Vue({
    el: "#app",
    delimiters: ["[[", "]]"],
    data: {
        title: "To Do List",
        toDos: [],
        search: '',
        create_title: '',
        create_description: ''
    },
    methods: {
        gettoDos: function() {
            axios({
                method: "get",
                url: '{% url "toDos:toDos" %}',
                params: {
                    search: this.search,
                    limit: 5
                }
            }).then((response) => {
                console.log(response.data);
                this.toDos = response.data.toDos
                this.total_pages = response.data.total_pages
            });
        },
        createContact: function() {
            if (this.create_name == '' || this.create_email == '') {
                alert('Please fill in all the fields!') // TODO: replace with toast
                return
            }
            axios({
                method: 'post',
                url: '{% url "toDos:create" %}',
                // use Django template rendering to get the csrf token into the request header
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}'
                },
                // Axios will turn this JavaScript object into JSON
                data: {
                    name: this.create_name,
                    email: this.create_email
                }
            }).then(response => {
                // console.log(response.data)
                // reset the form
                this.create_name = ''
                this.create_email = ''
                this.page = 1
                this.search = ''
                // get fresh data out of the database
                this.gettoDos()
            })
        },
        deleteContact: function(id) {
            console.log(id)
            axios({
                method: 'get',
                url: '{% url "toDos:delete" %}',
                params: {
                    id: id
                }
            }).then(response => {
                this.gettoDos()
            })
        },
        toggleFavorite: function(id) {
            axios({
                method: 'get',
                url: '{% url "toDos:toggle_favorite" %}',
                params: {
                    id: id
                }
            }).then(response => {
                // contact.favorited = !contact.favorited
                this.gettoDos()
            })
        }
    },
    created: function () {
        this.gettoDos()
    },
});