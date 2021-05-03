new Vue({

    el: '#orders_app',

    data: {
        orders: []
    },

    created: function () {
        const v = this;
        axios.get('/api/orders/')
        .then((res) => {
            v.orders = res.data
        })
    }

})