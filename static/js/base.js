$(document).ready(function(){
    $('.parallax').parallax();
    $('.dropdown-trigger').dropdown();
    $('.sidenav').sidenav();
    $('.modal').modal();
    $('select').formSelect();
});

$('.update-link').click(function(e) {
    var form = $(this).prev('.update-form');
    form.submit();
})
