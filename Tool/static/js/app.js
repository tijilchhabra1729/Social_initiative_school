$(window).on('load', ()=> {
    $('.loading-wrapper').fadeOut(1500);
})

//chat content
$("#r1").on("click", () => {
    $("#r1").addClass("active");
    $("#r2").removeClass("active");
    $("#r3").removeClass("active");
    $("#review2").css("opacity", 0);
    $("#review3").css("opacity", 0);
    $("#review1").css("opacity", 1);
})

$("#r2").on("click", () => {
    $("#r2").addClass("active");
    $("#review1").css("opacity", 0);
    $("#review3").css("opacity", 0);
    $("#review2").css("opacity", 1);
    $("#r1").removeClass("active");
    $("#r3").removeClass("active");
})

$("#r3").on("click", () => {
    $("#r3").addClass("active");
    $("#r2").removeClass("active");
    $("#r1").removeClass("active");
    $("#review1").css("opacity", 0);
    $("#review2").css("opacity", 0);
    $("#review3").css("opacity", 1);
})