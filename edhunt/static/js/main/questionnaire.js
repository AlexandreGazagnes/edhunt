// QUESTIONNAIRE
$(document).ready(function(){
    $("#ehSmartHuntButton").click(function(){
        $('#ehFreeHuntContent').slideUp("slow");
        $('#ehSmartHuntContent').slideDown("slow");
        $('#starsOne').slideDown("slow");
        $('#ehSmartHuntButton').slideUp("slow");   });

    $("#ehBigHuntButton").click(function(){
        $('#ehSmartHuntContent').slideUp("slow");
        $('#ehBigHuntContent').slideDown("slow");
        $('#starsTwo').slideDown("slow");
        $('#ehBigHuntButton').slideUp("slow");   });

    $("#ehProHuntButton").click(function(){
        $('#ehBigHuntContent').slideUp("slow");
        $('#ehProHuntContent').slideDown("slow");
        $('#starsThree').slideDown("slow");
        $('#ehProHuntButton').slideUp("slow");   });   });




// inscription
$(document).ready(function(){
    $(".ehEdhuntPlus").mouseover(function(){
        $(this).css("background-color", "var(--myBrown)")
        .css("color", "var(--myWhite)");     })
        .css("transition-duration", "0.3s");
    $(".ehEdhuntPlus").mouseout(function(){
        $(this).css("background-color", "white")
        .css("color", "var(--myBrown)")
        .css("transition-duration", "0.3s");;    });  });
