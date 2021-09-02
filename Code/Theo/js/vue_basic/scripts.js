var app = new Vue({
    el: '#app',
    data: {
      message: 'Hello Vue!'
    },
    methods: {
        methodName: function() {
            this.message = 'you clicked the button'
        }
    }

  })