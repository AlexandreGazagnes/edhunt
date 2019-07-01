// OFFRE
// offres
$(document).ready(function(){
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

    var height = window.innerHeight
    || document.documentElement.clientHeight
    || document.body.clientHeight;

    var feat_list = ['free','smart', 'big', 'pro'];
    if (width > 576) {
        feat_list.forEach(function(feat, idx){
            $("#"+feat+"ButtonLaptop").mouseover(function(){
                $("#defaultContentLaptop").hide();
                $("#"+ feat +"ContentLaptop").show();     });
            $("#"+feat+"ButtonLaptop").mouseout(function(){
                $("#"+ feat +"ContentLaptop").hide();
                $("#defaultContentLaptop").show();   });      });}
    else {
        feat_list.forEach(function(feat, idx){
            $("#"+feat+"ButtonMobile").click(function(){
                if ( 'none' == $("#"+feat+"ContentMobile").css("display")) {
                    $("#"+feat+"ContentMobile").slideDown();    }
                else {
                    $("#"+feat+"ContentMobile").slideUp();    } });});}});





// OFFRE2
$(document).ready(function(){
    $(".offre2Button2").click(function(){
        $('.offre2Row2').slideDown();
        $('.offre2Button2').slideUp();   });

    $(".offre2Button3").click(function(){
        $('.offre2Row3').slideDown();
        $('.offre2Button3').slideUp();   });

    $(".offre2Button4").click(function(){
        $('.offre2Row4').slideDown();
        $('.offre2Button4').slideUp();   });    });




// // freeHunt
// $(document).ready(function(){
//   $("#freeCard").click(function(){

//     // reset all features
//     $(".myCard").attr("class", "myCard");
//     $(".myCardSelected").attr("class", "myCard");
//     $(".myCardTitle").attr("class", "myCardTitle");
//     $(".myCardTitleSelected").attr("class", "myCardTitle");
//     $(".myCardPrice").attr("class", "myCardPrice");
//     $(".myCardPriceSelected").attr("class", "myCardPrice");
//     $("#freeContent").slideUp();
//     $("#bigContent").slideUp();
//     $("#proContent").slideUp();
//     $("#smartContent").slideUp();

//     // change needed
//     $("#freeCard").attr("class", "myCardSelected");
//     $("#freeCardTitle").attr("class", "myCardTitleSelected");
//     $("#freeCardPrice").attr("class", "myCardPriceSelected");
//     $("#freeContent").slideDown();
//   });
// });


// // smartHunt
// $(document).ready(function(){
//   $("#smartCard").click(function(){

//     // reset all features
//     $(".myCard").attr("class", "myCard");
//     $(".myCardSelected").attr("class", "myCard");
//     $(".myCardTitle").attr("class", "myCardTitle");
//     $(".myCardTitleSelected").attr("class", "myCardTitle");
//     $(".myCardPrice").attr("class", "myCardPrice");
//     $(".myCardPriceSelected").attr("class", "myCardPrice");
//     $("#freeContent").slideUp();
//     $("#bigContent").slideUp();
//     $("#proContent").slideUp();
//     $("#smartContent").slideUp();

//     // change needed
//     $("#smartCard").attr("class", "myCardSelected");
//     $("#smartCardTitle").attr("class", "myCardTitleSelected");
//     $("#smartCardPrice").attr("class", "myCardPriceSelected");
//     $("#smartContent").slideDown();
//   });
// });


// // bigHunt
// $(document).ready(function(){
//   $("#bigCard").click(function(){

//     // reset all features
//     $(".myCard").attr("class", "myCard");
//     $(".myCardSelected").attr("class", "myCard");
//     $(".myCardTitle").attr("class", "myCardTitle");
//     $(".myCardTitleSelected").attr("class", "myCardTitle");
//     $(".myCardPrice").attr("class", "myCardPrice");
//     $(".myCardPriceSelected").attr("class", "myCardPrice");
//     $("#freeContent").slideUp();
//     $("#bigContent").slideUp();
//     $("#proContent").slideUp();
//     $("#smartContent").slideUp();

//     // change needed
//     $("#bigCard").attr("class", "myCardSelected");
//     $("#bigCardTitle").attr("class", "myCardTitleSelected");
//     $("#bigCardPrice").attr("class", "myCardPriceSelected");
//     $("#bigContent").slideDown();
//   });
// });


// // proHunt
// $(document).ready(function(){
//   $("#proCard").click(function(){

//     // reset all features
//     $(".myCard").attr("class", "myCard");
//     $(".myCardSelected").attr("class", "myCard");
//     $(".myCardTitle").attr("class", "myCardTitle");
//     $(".myCardTitleSelected").attr("class", "myCardTitle");
//     $(".myCardPrice").attr("class", "myCardPrice");
//     $(".myCardPriceSelected").attr("class", "myCardPrice");
//     $("#freeContent").slideUp();
//     $("#bigContent").slideUp();
//     $("#proContent").slideUp();
//     $("#smartContent").slideUp();

//     // change needed
//     $("#proCard").attr("class", "myCardSelected");
//     $("#proCardTitle").attr("class", "myCardTitleSelected");
//     $("#proCardPrice").attr("class", "myCardPriceSelected");
//     $("#proContent").slideDown();
//   });
// });
