$(document).ready(function ($) {
    var activePage = window.location.href;
    $('.nav-item a').each(function () {
        var linkPage = this.href;

        if (activePage == linkPage) {
            $(this).closest("li").addClass("active");
        }
    });
    console.log('Page loaded');
});