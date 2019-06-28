// loadingButton
function loadingButton() {
      var clicked = document.getElementById("clicked");
      var notClicked = document.getElementById("notClicked");
          clicked.style.display = "block";
          notClicked.style.display = "none";
    }


// manage buttons
function buttonChanger(x, y, z){
    $("#" + x + "Button").click(function(){
        if ( $(this).attr('class') == 'ehTildeOn') {
            $(this).removeClass().addClass('ehTildeOff');
            $("#" + x + "Content").slideUp();    }
        else {
            $("#" + y + "Content").slideUp();
            $("#" + z + "Content").slideUp();
            $(this).removeClass().addClass('ehTildeOn');
            $("#" + x + "Content").slideDown();
            $("#" + y + "Button").removeClass().addClass('ehTildeOff');
            $("#" + z + "Button").removeClass().addClass('ehTildeOff');   }})}


function buttonManager(x, y, z){
    buttonChanger(x, y, z);
    buttonChanger(y, x, z);
    buttonChanger(z, y, x) }


// nav and opt
function navChanger(x){
        $("#"+x+"Button").removeClass().addClass('ehTildeOn');
        $("#" + x + "Content").slideDown();     }


function navManager(x){
    var array1 = ['apec', 'cadremploi', 'indeed', 'jobintree', 'keljob',
    'lesjeudi', 'monster', 'meteojob', 'regionjob'];
    array1.forEach(function(element) {
        if (x == element) {
             navChanger(x);}    });    }


// main
$(function(){
    var x = $("#ehNav").html();
    navManager(x);})


$(function(){
    buttonManager('apec', 'cadremploi', 'indeed');
    buttonManager('jobintree', 'keljob', 'lesjeudis');
    buttonManager('meteojob', 'monster', 'regionjob');  })



