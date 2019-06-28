function myFieldManager(x){
    $(function(){
        $("#"+x+"ShowButton").click(function(){
              $("#"+x+"ShowButton").slideUp();
              $("#"+x+"Content").slideDown();     });});
    $(function(){
        $("#"+x+"HideButton").click(function(){
            $("#"+x+"Content").slideUp();
            $("#"+x+"ShowButton").slideDown();     });});
    $(function(){
        $("#"+x+"HideButton1").click(function(){
            $("#"+x+"Content").slideUp();
            $("#"+x+"ShowButton").slideDown();     });});
    $(function(){
        $("#"+x+"HideButton2").click(function(){
            $("#"+x+"Content").slideUp();
            $("#"+x+"ShowButton").slideDown();     });});    }


// main
$(function() {
    var fields =["profile", "plateform", "searchs", "opp"];
    fields.forEach(function(element) {
        myFieldManager(element)    ;})   ;})




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
