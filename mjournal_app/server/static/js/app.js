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

app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    router: router,

    data: strings,

    simplemde: null,
    entryID: null,

    methods: {
        initIndexPage: function() {
            $.get('ajax/getEntries', function(result) {
                console.log(result);
            });
            $('#calendar').datepicker();
        },

        initWritePage: function() {
            d = new Date();
            this.entryID = d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate();

            this.simplemde = new SimpleMDE({
                element: document.getElementById('write-area'),

                autosave: {
                    enabled: true,
                    uniqueId: this.entryID
                },

                toolbar: [
                    'bold',
                    'italic',
                    'strikethrough',
                    'heading',
                    '|',
                    'image',
                    'quote',
                    'unordered-list',
                    'ordered-list',
                    '|',
                    'undo',
                    'redo',
                    {
                        name: 'save',
                        action: function() {
                            app.save();
                        },
                        className: 'fa fa-save',
                        title: 'Save'
                    }
                ],

                autoDownloadFontAwesome: false
            });

            strings.entry_title = new Date().toDateString();
        },

        onPageLoad: function(path) {
            switch(path) {
                case '/':
                    this.initIndexPage();
                    break;
                case '/write':
                    this.initWritePage();
                    break;
            }
        },

        save: function() {
            $.post('ajax/save', {
                id: app.entryID,
                content: app.simplemde.value()
            }, function(d) {
                console.log(d);
            });
        }
    },

    mounted: function() {
        this.onPageLoad(this.$route.path);
    },

    updated: function() {
        this.onPageLoad(this.$route.path);
    },
});
