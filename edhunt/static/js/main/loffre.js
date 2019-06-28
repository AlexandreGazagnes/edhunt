// freeHunt
$(document).ready(function(){
  $("#freeCard").click(function(){

    // reset all features
    $(".myCard").attr("class", "myCard");
    $(".myCardSelected").attr("class", "myCard");
    $(".myCardTitle").attr("class", "myCardTitle");
    $(".myCardTitleSelected").attr("class", "myCardTitle");
    $(".myCardPrice").attr("class", "myCardPrice");
    $(".myCardPriceSelected").attr("class", "myCardPrice");
    $("#freeContent").slideUp();
    $("#bigContent").slideUp();
    $("#proContent").slideUp();
    $("#smartContent").slideUp();

    // change needed
    $("#freeCard").attr("class", "myCardSelected");
    $("#freeCardTitle").attr("class", "myCardTitleSelected");
    $("#freeCardPrice").attr("class", "myCardPriceSelected");
    $("#freeContent").slideDown();
  });
});


// smartHunt
$(document).ready(function(){
  $("#smartCard").click(function(){

    // reset all features
    $(".myCard").attr("class", "myCard");
    $(".myCardSelected").attr("class", "myCard");
    $(".myCardTitle").attr("class", "myCardTitle");
    $(".myCardTitleSelected").attr("class", "myCardTitle");
    $(".myCardPrice").attr("class", "myCardPrice");
    $(".myCardPriceSelected").attr("class", "myCardPrice");
    $("#freeContent").slideUp();
    $("#bigContent").slideUp();
    $("#proContent").slideUp();
    $("#smartContent").slideUp();

    // change needed
    $("#smartCard").attr("class", "myCardSelected");
    $("#smartCardTitle").attr("class", "myCardTitleSelected");
    $("#smartCardPrice").attr("class", "myCardPriceSelected");
    $("#smartContent").slideDown();
  });
});


// bigHunt
$(document).ready(function(){
  $("#bigCard").click(function(){

    // reset all features
    $(".myCard").attr("class", "myCard");
    $(".myCardSelected").attr("class", "myCard");
    $(".myCardTitle").attr("class", "myCardTitle");
    $(".myCardTitleSelected").attr("class", "myCardTitle");
    $(".myCardPrice").attr("class", "myCardPrice");
    $(".myCardPriceSelected").attr("class", "myCardPrice");
    $("#freeContent").slideUp();
    $("#bigContent").slideUp();
    $("#proContent").slideUp();
    $("#smartContent").slideUp();

    // change needed
    $("#bigCard").attr("class", "myCardSelected");
    $("#bigCardTitle").attr("class", "myCardTitleSelected");
    $("#bigCardPrice").attr("class", "myCardPriceSelected");
    $("#bigContent").slideDown();
  });
});


// proHunt
$(document).ready(function(){
  $("#proCard").click(function(){

    // reset all features
    $(".myCard").attr("class", "myCard");
    $(".myCardSelected").attr("class", "myCard");
    $(".myCardTitle").attr("class", "myCardTitle");
    $(".myCardTitleSelected").attr("class", "myCardTitle");
    $(".myCardPrice").attr("class", "myCardPrice");
    $(".myCardPriceSelected").attr("class", "myCardPrice");
    $("#freeContent").slideUp();
    $("#bigContent").slideUp();
    $("#proContent").slideUp();
    $("#smartContent").slideUp();

    // change needed
    $("#proCard").attr("class", "myCardSelected");
    $("#proCardTitle").attr("class", "myCardTitleSelected");
    $("#proCardPrice").attr("class", "myCardPriceSelected");
    $("#proContent").slideDown();
  });
});
