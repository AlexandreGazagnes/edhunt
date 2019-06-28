
function updateResponsiveContainer() {
    var cont = document.getElementById('responsiveContainer')
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

    if (width > 1200) {
        cont.className = "container"
    } else {
                cont.className = "container-fluid"
    }

  }

function myAlert() {
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;
    alert("width changed  : " + width ) ;
}

// go back
function goBack() {
  window.history.go(-1);
}



// manage Responsive Button
function giveWindowSize() {
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;
    var height = window.innerHeight
    || document.documentElement.clientHeight
    || document.body.clientHeight;

    $("#windowSize").html("w: " + width + "px / h: "+ height); }



// main
$(function(){
    giveWindowSize();
    $(window).resize(function() {
        giveWindowSize();}) ;   })
