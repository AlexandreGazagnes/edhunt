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
