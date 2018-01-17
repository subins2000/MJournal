const router = new VueRouter({
    mode: 'history',
    base: '/',
    routes: [{
        path: '/',
        component: Home
    }, {
        path: '/write',
        component: Write
    }, {
        path: '/settings',
        component: Settings
    }]
})

var app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    router: router,

    data: {
        name: 'MJournal'
    },

    methods: {

    }
})
