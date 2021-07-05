// back to top button
//Make sure the user has scrolled at least 1.5x the height of the browser
var toggleHeight = $(window).outerHeight() * 1;

$(window).scroll(function() {
    if ($(window).scrollTop() > toggleHeight) {
        //Adds active class to make button visible
        $(".m-backtotop ").addClass("active ");

    } else {
        //Removes active class to make button visible
        $(".m-backtotop ").removeClass("active ");


    }
});

//Scrolls the user to the top of the page again
$(".m-backtotop ").click(function() {
    $("html, body ").animate({
        scrollTop: 0
    }, "slow ");
    return false;
});