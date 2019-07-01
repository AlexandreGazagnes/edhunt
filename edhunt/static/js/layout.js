function goBack() {
    window.history.go(-1);    }


function updateResponsiveContainer() {
    var cont = document.getElementById('responsiveContainer')
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

    if (width > 1200) {
        cont.className = "container"     }
    else {
                cont.className = "container-fluid"   }    }


function giveWindowSize() {
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;
    var height = window.innerHeight
    || document.documentElement.clientHeight
    || document.body.clientHeight;

    $("#windowSize").html("w: " + width + "px / h: "+ height);    }



// main
$(function(){
    giveWindowSize();
    updateResponsiveContainer();
    $(window).resize(function() {
        updateResponsiveContainer();
        giveWindowSize();}) ;   })

