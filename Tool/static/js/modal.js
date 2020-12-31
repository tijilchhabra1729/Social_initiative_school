$('.btn-cta').on('click', () => {
    $('.submitted').addClass('open');
    $('.submitted__modal').addClass('open__modal');
})

$('.cross').on('click', () => {
    $('.submitted').removeClass('open');
    $('.submitted__modal').removeClass('open__modal');
})