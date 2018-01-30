var strings = {
    name: 'MJournal',
    entry_title: ''
};

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

    data: strings,

    methods: {
        initWritePage: function() {
            var simplemde = new SimpleMDE({
                element: document.getElementById('write-area')
            });

            strings.entry_title = new Date().toDateString();
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
