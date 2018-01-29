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
    }],
    ready: function(from) {
        console.log(from);
    }
});

var app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    router: router,

    data: {
        name: 'MJournal'
    },

    methods: {
        initWritePage: function() {
            var simplemde = new SimpleMDE({
                element: document.getElementById('write-area')
            });
        },

        onPageLoad: function(path) {
            if (path === '/write') {
                this.initWritePage();
            }
        }
    },

    watch: {
        '$route': function(to) {
            this.onPageLoad(to.path);
        }
    },

    mounted: function() {
        this.onPageLoad(this.$route.path);
    },

    updated: function() {
        this.onPageLoad(this.$route.path);
    }
});
