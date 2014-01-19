(function () {

var DEFAULT_SCROLL_TIME = 700;
var $body;
var $header;
var $logo;

$(function () {
    $body = $('body');
    $header = $('header');
    $logo = $('.logo');
    $('#menu a').click(function () {
        var href = $(this).attr('href'),
            $elem = href !== '#' && $(href) || $('body');
        smoothScrollTo($elem);
        return false;
    });
    $(window).scroll(function () {
        var doc = document.documentElement;
        var top = (window.pageYOffset || doc.scrollTop)  - (doc.clientTop || 0);
        $logo.toggle(top < 40);
    });
});

function smoothScrollTo($elem, t, ease) {
    t = t || DEFAULT_SCROLL_TIME;
    ease = ease || 'easeInOutQuart';
    console.log(t, ease, $elem.position().top, menuHeight());
    $body.stop().animate({
        scrollTop: $elem.position().top - menuHeight()
    }, t, ease);
}

function menuHeight() {
    return $header.height();
}

}());
