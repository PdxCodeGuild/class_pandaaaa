let app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue',
        clicks: 0
    },
    methods: {
       reverseMessage: function () {
           this.message = this.message.split('').reverse().join('')
           this.clicks += 1
       } 
    }
})