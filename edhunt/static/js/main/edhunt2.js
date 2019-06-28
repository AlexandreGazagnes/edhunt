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


// manage Responsive Button
function changeActionText() {
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

    if (width > 480) {
        $(".ACTION").html("Action"); }
    else {
        $('.ACTION').html("");  }     }


// hide /wrap /cup text elem for responsive tables
function cutProfileTheadText() {
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;
    if (width < 580) {
        $("#expectationHead").html("Atts.");
        $("#identificationHead").html("Id.");
        $("#localisationHead").html("Loc.");
        $("#diplomaHead").html("Form.");
        $("#work_experienceHead").html("Prof.");
        $("#work_statusHead").html("Stat.");
        $("#languageHead").html("Lang."); }
    else {
        $("#expectationHead").html("Attentes");
        $("#identificationHead").html("Identité");
        $("#localisationHead").html("Localistation");
        $("#diplomaHead").html("Formation");
        $("#work_experienceHead").html("Experience Prof.");
        $("#work_statusHead").html("Status");
        $("#languageHead").html("Langues");  }   }

function hideTable600() {
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;
    if (width < 600) {
        $(".HIDE600").css("display","none");}
    else {
        $(".HIDE600").css("display","");}  }

function hideTable400() {
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;
    if (width < 400) {
        $(".HIDE400").css("display","none");}
    else {
        $(".HIDE400").css("display","");}  }

function hideTable800() {
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;
    if (width < 820) {
        $(".HIDE800").css("display","none");}
    else {
        $(".HIDE800").css("display","");}  }

// main
$(function(){
    buttonManager('profile', 'plateform', 'search');
    buttonManager('piste', 'opportunity', 'candidature');
    changeActionText();
    cutProfileTheadText();
    hideTable800();
    hideTable600();
    hideTable400();
    $(window).resize(function() {
        changeActionText();
        hideTable800();
        hideTable600();
        hideTable400();
        cutProfileTheadText();})    })


// function myFieldManager(x){
//     $(function(){
//         $("#"+x+"ShowButton").click(function(){
//               $("#"+x+"ShowButton").slideUp();
//               $("#"+x+"Content").slideDown();     });});
//     $(function(){
//         $("#"+x+"HideButton").click(function(){
//             $("#"+x+"Content").slideUp();
//             $("#"+x+"ShowButton").slideDown();     });});
//     $(function(){
//         $("#"+x+"HideButton1").click(function(){
//             $("#"+x+"Content").slideUp();
//             $("#"+x+"ShowButton").slideDown();     });});
//     $(function(){
//         $("#"+x+"HideButton2").click(function(){
//             $("#"+x+"Content").slideUp();
//             $("#"+x+"ShowButton").slideDown();     });});    }


// // main
// $(function() {
//     var fields =["profile", "plateform", "searchs", "opp"];
//     fields.forEach(function(element) {
//         myFieldManager(element)    ;})   ;})




// // profile
// $(document).ready(function(){
//   $("#profileShowButton").click(function(){
//     $(this).slideUp();
//     $("#profileContent").slideDown();
//   });
// });
// $(document).ready(function(){
//   $("#profileHideButton").click(function(){
//     $("#profileContent").slideUp();
//     $("#profileShowButton").slideDown();
//   });
// });




// $(document).ready(function(){
//   $("#profileHideButton").click(function(){
//     $("#profileContent").slideUp();
//     $("#profileShowButton").show();
//   });
// });


// // plateform
// $(document).ready(function(){
//   $("#plateformShowButton").click(function(){
//     $(this).hide();
//     $("#plateformContent").show();
//   });
// });
// $(document).ready(function(){
//   $("#plateformHideButton").click(function(){
//     $("#plateformContent").hide();
//     $("#plateformShowButton").show();
//   });
// });


// // searchs
// $(document).ready(function(){
//   $("#searchsShowButton").click(function(){
//     $(this).hide();
//     $("#searchsContent").show();
//   });
// });
// $(document).ready(function(){
//   $("#searchsHideButton").click(function(){
//     $("#searchsContent").hide();
//     $("#searchsShowButton").show();
//   });
// });


// // searchs
// $(document).ready(function(){
//   $("#oppShowButton").click(function(){
//     $(this).hide();
//     $("#oppContent").show();
//   });
// });
// $(document).ready(function(){
//   $("#oppHideButton").click(function(){
//     $("#oppContent").hide();
//     $("#oppShowButton").show();
//   });
// });


// // function swapProfile(){
// //   var pro = document.getElementById("profilContent");
// //   if (pro.style.display == "block") {
// //     pro.style.display = 'none' ;
// //   } else {
// //     pro.style.display = 'block' ;
// //   }
// // }


// // function swapSearchs(){
// //   var sea = document.getElementById("searchsContent");
// //   if (sea.style.display == "block") {
// //     sea.style.display = 'none' ;
// //   } else {
// //     sea.style.display = 'block' ;
// //   }
// // }


// // function swapOpp(){
// //   var opp = document.getElementById("oppContent");
// //   if (opp.style.display == "block") {
// //     opp.style.display = 'none' ;
// //   } else {
// //     opp.style.display = 'block' ;
// //   }
// // }


// // function swapPlateform(){
// //   var opp = document.getElementById("plateformContent");
// //   if (opp.style.display == "block") {
// //     opp.style.display = 'none' ;
// //   } else {
// //     opp.style.display = 'block' ;
// //   }
// // }
