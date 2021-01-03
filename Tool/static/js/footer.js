$(window).resize(function(){
    if(window.innerWidth < 1000) {
        $('.footer').css('opacity', 0);
    } else {
        $('.footer').css('opacity', 1);
    }
});