var modcards = {}
var modcard

ModCard = Backbone.View.extend({
    events: {
        'click .quit': 'quitclicked',
        'click': 'clicked',
        'click .flipper': 'flipclicked'
    },
    data: function() {
        return {username: 'test',
                linkkarma: 10,
                commentkarma: 200}
    },
    flipclicked: function(e) {
        e.preventDefault()
        this.flip()
    },
    quitclicked: function(e) {
        e.preventDefault()
        this.hide()
    },
    clicked: function(e) {e.stopPropagation()},
    render: function() {
        this.$el.data('modcard', this)
        this.$el.addClass('flippable modcard')
        this.$el.html(r.templates.make('templates/modcard', this.data()))
        return this
    },
    isvisible: function() {
        return this.$el.is(':visible')
    },
    isflipped: function() {
        return this.$el.hasClass('flipped')
    },
    hide: function() {
        this.$el.hide(80)
        modcard = null
        return this
    },
    front: function() {
        this.$el.removeClass('flipped')
        return this
    },
    back: function() {
        this.$el.addClass('flipped')
        return this
    },
    show: function(x, y) {
        if(modcard) {modcard.hide()}
        modcard = this
        this.$el.css('top', y)
        this.$el.css('left', x)
        this.$el.show(40)
        return this
    },
    flip: function() {
        if(this.isflipped()) {
            this.front()
        } else {
            this.back()
        }
        return this
    }
})

ModCarder = Backbone.View.extend({
    events: {
        'click': 'expandclicked'
    },
    expandclicked: function(e) {
        e.preventDefault()
        e.stopPropagation()
        this.expand(e.pageX, e.pageY)
    },
    expand: function(x, y) {
        if(!this.modcard) {
            this.init()
        }
        this.modcard.show(x, y)
    },
    init: function() {
        var name = 'test'
        var modcard = modcards[name]
        if(modcard) {
            this.modcard = modcard
        } else {
            var $modcard = $('<div>');
            this.modcard = this.create($modcard)
            $modcard.insertAfter(this.$el)
            modcards[name] = this.modcard
        }
        return this
    },
    create: function(el) {
        return new ModCard({el: el}).render()
    }
})

$('html').on('click', function() {
    if(modcard) {modcard.hide()}
})

$(function() {
    $('.modcarder').each(function(idx, el) {
        $(el).data('ModCarder', new ModCarder({el: el}))
    })
})
