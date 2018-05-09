//a object literal
var backLink = {
    init: function(settings) {
        backLink.config = {
            items: $(".second-back a:first , .first-back a:first")
        };
        //Allow ovrriding the default setting
        $.extend(backLink.config, settings);
        backLink.setup();
    },
    setup: function() {
        backLink.config.items.each(backLink.hover);
    },
    hover: function() {
        var $item = $(this);
        $item.hover(backLink.in, backLink.out);
    },
    in: function() {
        var $item = $(this);
        $item.stop(true).animate({
            opacity: 0.5
        }, 500);
    },
    out: function() {
        var $item = $(this);
        $item.stop(true).animate({
            opacity: 1
        }, 500);
    }
};


$(document).ready(function() {

    backLink.init();



    // check if logged in

    var firstRow = $('.first-row');
    var firstRowImg = $('.first-row div.btn-img');
    var firstRowText = $('.first-row .first-back');
    var secondRow = $('.second-row');
    var secondRowImg = $('.second-row div.btn-img');
    var secondRowText = $('.second-row .second-back');

    $(window).scroll(function(event) {

        if ($(window).scrollTop() >= $(firstRow).offset().top && $(window).scrollTop() < $(firstRow).offset().top + $(firstRowText).height()) {

            $(firstRowText).addClass('exchange-left');
            $(firstRowImg).addClass('exchange-right');


        } else if ($(window).scrollTop() > = $(secondRow).offset().top && $(window).scrollTop() < $(secondRow).offset().top + $(secondRowText).height()) {

            $(secondRowText).addClass('exchange-right');
            $(secondRowImg).addClass('exchange-left');


        } else {

            $(firstRowText).removeClass('exchange-left');
            $(firstRowImg).removeClass('exchange-right');

            $(secondRowText).removeClass('exchange-right');
            $(secondRowImg).removeClass('exchange-left');

        }
    });

});