// inscription
$(document).ready(function(){
    $(".ehInscriptionSmall").mouseover(function(){
        $(this).css("background-color", "var(--myBrown)")
        .css("color", "var(--myWhite)");     })
        .css("transition-duration", "0.3s");
    $(".ehInscriptionSmall").mouseout(function(){
        $(this).css("background-color", "var(--myWhite)")
        .css("color", "var(--myBrown)")
        .css("transition-duration", "0.3s");;    });  });


// ehTextBoxGridNeuf
$(document).ready(function(){
  $(".ehTextBoxGridNeuf").mouseover(function(){
    $(this).css("background-color", "var(--myBrown)")
    .css("color", "var(--myWhite)")
    .css("transition-duration", "0.3s");;
  });
  $(".ehTextBoxGridNeuf").mouseout(function(){
    $(this).css("background-color", "var(--myWhite)")
    .css("color", "var(--myBrown)")
    .css("transition-duration", "0.3s");   });   });


// ehTextBox3
$(document).ready(function(){
  $(".ehTextBox3").mouseover(function(){
    $(this).css("background-color", "var(--myBrown)")
    .css("color", "var(--myWhite)")
    .css("transition-duration", "0.3s");;
  });
  $(".ehTextBox3").mouseout(function(){
    $(this).css("background-color", "var(--myWhite)")
    .css("color", "var(--myBrown)")
    .css("transition-duration", "0.3s");   });    });


// foot
$(document).ready(function(){
    $(".ehTextBoxFoot").mouseover(function(){
        $(this).css("background-color", "var(--myBrown)")
        .css("color", "var(--myWhite)")
        .css("transition-duration", "0.3s");     });
    $(".ehTextBoxFoot").mouseout(function(){
        $(this).css("background-color", "var(--myWhite)")
        .css("color", "var(--myBrown)")
        .css("transition-duration", "0.3s");    });   });


//responsive Box
function showResponsiveTopBox() {
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

    var height = window.innerHeight
    || document.documentElement.clientHeight
    || document.body.clientHeight;

    if (width > 576) {
        $(".ehResponsiveTopBox").css("height", "0px").hide();
        $(".ehResponsiveSecondBox").css("height", "0px").hide();}
    else if (width > 400) {
        $(".ehResponsiveTopBox").css("height", "50px").show();
        $(".ehResponsiveSecondBox").css("height", "30px").show();}
    else {
        if(height < 530){
            $(".ehResponsiveTopBox").css("height", "0px").hide();
            $(".ehResponsiveSecondBox").css("height", "0px").hide();
            $(".ehTextBoxTop").css("padding-top", "0px")
            .css("padding-bottom", "90px");
        }
        else {
            $(".ehInscriptionSmall").css("margin", "0px 0px 50px 0px")
            $(".ehH1").css("padding", "10px 0px").css("margin", "0px")
            $(".ehH2").css("padding", "10px 0px").css("margin", "0px")
            $(".ehTextBoxTop").css("padding", "5px 0px").css("margin", "0px")
            $(".ehResponsiveTopBox").css("height", "0px").css("padding", "0px 0px").show();
            $(".ehResponsiveSecondBox").css("height", "30px").show();}  ;};}


function manageResponsiveBlock() {
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

    var height = window.innerHeight
    || document.documentElement.clientHeight
    || document.body.clientHeight;

    if (width > 576) {
        $(".ehLaptop").show();
        $(".ehMobile").hide();}
    else {
        $(".ehLaptop").hide();
        $(".ehMobile").show();}; }


function show576() {
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

    var height = window.innerHeight
    || document.documentElement.clientHeight
    || document.body.clientHeight;

    if (width < 576) {
        $(".show576").show();}
    else {
        $(".show576").hide();}  }


function hide576() {
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

    var height = window.innerHeight
    || document.documentElement.clientHeight
    || document.body.clientHeight;

    if (width < 576) {
        $(".hide576").hide();}
    else {
        $(".hide576").show();}  }


function swapOrder(x) {
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

    var height = window.innerHeight
    || document.documentElement.clientHeight
    || document.body.clientHeight;
    if (width < x) {
        $(".swap"+x).addClass("order-first");}
    else {
        $(".swap"+x).removeClass("order-first");}  }



// main
$(function(){
    hide576();
    show576();
    showResponsiveTopBox();
    manageResponsiveBlock();
    swapOrder(576);
    swapOrder(768);
    $(window).resize(function() {
        hide576();
        show576();
        showResponsiveTopBox();
        manageResponsiveBlock();
        swapOrder(576);
        swapOrder(768);})    })
