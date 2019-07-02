function goUp() {
    $('html,body').animate({scrollTop: 0}, 'slow');}

function goDown() {
    $('html,body').animate({scrollDown: 100}, 'slow');}

function goBack() {
    window.history.go(-1);    }

function goBack() {
    window.history.go(-1);    }


function updateResponsiveContainer() {
    var cont = document.getElementById('responsiveContainer')
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

    if (cont) {
        if (width > 1200) {
            cont.className = "container"     }
        else {
            cont.className = "container-fluid"   } }    }


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

