// manage buttons
function buttonChanger(x, y){
    $("#" + x + "Button").click(function(){
        if ( $(this).attr('class') == 'ehTildeOn') {
            $(this).removeClass().addClass('ehTildeOff');
            $("#" + x + "Content").slideUp();    }
        else {
            $("#" + y + "Content").slideUp();
            $(this).removeClass().addClass('ehTildeOn');
            $("#" + x + "Content").slideDown();
            $("#" + y + "Button").removeClass().addClass('ehTildeOff');   }})}


function buttonManager(x, y){
    buttonChanger(x, y);
    buttonChanger(y, x);}



// nav and opt
function navChanger(x){
        $("#"+x+"Button").removeClass().addClass('ehTildeOn');
        $("#" + x + "Content").slideDown();     }


function navManager(x){
    var array1 = ['essentiel', 'job', 'status', 'language'];
    array1.forEach(function(element) {
        if (x == element) {
             navChanger(x);}    });    }

// main
$(function(){
    var x = $("#ehNav").html();
    navManager(x);})

$(function(){
    buttonManager('essentiel', 'job');
    buttonManager('status', 'language');  })
