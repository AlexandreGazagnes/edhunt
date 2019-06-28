function myFieldManager(x){
  $(function(){
        $("#"+x+"ShowButton").click(function(){
      $("#"+x+"Head").slideUp();
      $("#"+x+"Content").slideDown();
    });
  });
  $(function(){
    $("#"+x+"HideButton").click(function(){
      $("#"+x+"Content").slideUp();
      $("#"+x+"Head").slideDown();
    });
  });}


// main
$(function() {
    var fields =["resume", "account", "expectation", "identification",
                 "localisation", "diploma", "work_experience",
                 "work_status", "language"];
    fields.forEach(function(element) {
        myFieldManager(element);});})





// $(function(){
//       $("#resumeShowButton").click(function(){
//     $("#resumeHead").slideUp();
//     $("#resumeContent").slideDown();
//   });
// });
// $(function(){
//   $("#resumeHideButton").click(function(){
//     $("#resumeContent").slideUp();
//     $("#resumeHead").slideDown();
//   });
// });


// // resume
// $(function(){
//       $("#accountShowButton").click(function(){
//     $("#accountHead").slideUp();
//     $("#accountContent").slideDown();
//   });
// });
// $(function(){
//   $("#accountHideButton").click(function(){
//     $("#accountContent").slideUp();
//     $("#accountHead").slideDown();
//   });
// });





// function myShow(x){
//       $( "#"+x+"Field" ).hover(
//           function()
//               {$( "#"+x+"Head" ).slideUp();},
//           function()
//               {$( "#"+x+"Head" ).slideDown();});}

// function myHide(x){
//       $( "#"+x+"Field" ).hover(
//           function()
//               {$( "#"+x+"Content" ).slideDown();},
//           function()
//               {$( "#"+x+"Content"  ).slideUp();});  }

// function myFieldManager(x){
//     $( "#"+x+"Field" ).hover(
//       myShow(x),
//       myHide(x))}

// main
// $(function() {
//     var fields =["resume", "account", "expectation", "identification",
//                  "localisation", "diploma", "work_experience",
//                  "work_status", "language"];
//     fields.forEach(function(element) {
//         myFieldManager(element);});})


// $(function() {
//     $( "#accountField" ).hover(
//         function()
//             {$( "#accountHead" ).slideUp();},
//         function()
//             {$( "#accountHead" ).slideDown();});})

// $(function() {
//     $( "#accountField" ).hover(
//         function()
//             {$( "#accountContent" ).slideDown();},
//         function()
//             {$( "#accountContent"  ).slideUp();});  })

// $(function() {
//     $( "#accountField" ).hover(
//         function()
//             {$( "#accountHead" ).slideUp();},
//         function()
//             {$( "#accountHead" ).slideDown();});})

// $(function() {
//     $( "#accountField" ).hover(
//         function()
//             {$( "#accountContent" ).slideDown();},
//         function()
//             {$( "#accountContent"  ).slideUp();});  })






// $(function() {
//     $( "#resumeField" ).hover(
//         function()
//             {$( "#resumeHead" ).slideUp();},
//         function()
//             {$( "#resumeHead" ).slideDown();});})

// $(function() {
//     $( "#resumeField" ).hover(
//         function()
//             {$( "#resumeContent" ).slideDown();},
//         function()
//             {$( "#resumeContent" ).slideUp();});})



// function expandresumeOption() {
//       var opt = document.getElementById("resumeOption");
//       var btn = document.getElementById("resumeButton")
//       if (opt.style.display == "none"){
//           opt.style.display = "block";
//           btn.style.display = "none";}
//   }


// onmouseover="showFunct('resumeOption')"  onmouseout="hideFunct('resumeOption')


// function showFunct(x){
  // $("#"+ x +"Head").slideUp();
  // // document.getElementById(x +"Head").style.display = "none";
  // $("#"+ x +"Content").slideDown();
  // // document.getElementById(x +"Content").style.display = "block";
// }

// function hideFunct(x){
  // $("#"+ x +"Head").slideDown();
  // // document.getElementById(x +"Head").style.display = "none";
  // $("#"+ x +"Content").slideUp();
  // // document.getElementById(x +"Content").style.display = "block";
// }


// // account
// function expandaccountOption() {
//       var opt = document.getElementById("accountOption");
//       var btn = document.getElementById("accountButton")
//       if (opt.style.display == "none"){
//           opt.style.display = "block";
//           btn.style.display = "none";}
//   }

// function reduceaccountOption() {
//       var opt = document.getElementById("accountOption");
//       var btn = document.getElementById("accountButton")
//       if (opt.style.display == "block"){
//           opt.style.display = "none";
//           btn.style.display = "block";}
//     }

// // expectations
// function expandexpectationOption() {
//       var opt = document.getElementById("expectationOption");
//       var btn = document.getElementById("expectationButton")
//       if (opt.style.display == "none"){
//           opt.style.display = "block";
//           btn.style.display = "none";}
//   }

// function reduceexpectationOption() {
//       var opt = document.getElementById("expectationOption");
//       var btn = document.getElementById("expectationButton")
//       if (opt.style.display == "block"){
//           opt.style.display = "none";
//           btn.style.display = "block";}
//     }


// function reduceresumeOption() {
//       var opt = document.getElementById("resumeOption");
//       var btn = document.getElementById("resumeButton")
//       if (opt.style.display == "block"){
//           opt.style.display = "none";
//           btn.style.display = "block";}
//     }

// // identity
// function expandidentificationOption() {
//       var opt = document.getElementById("identificationOption");
//       var btn = document.getElementById("identificationButton")
//       if (opt.style.display == "none"){
//           opt.style.display = "block";
//           btn.style.display = "none";}
//   }

// function reduceidentificationOption() {
//       var opt = document.getElementById("identificationOption");
//       var btn = document.getElementById("identificationButton")
//       if (opt.style.display == "block"){
//           opt.style.display = "none";
//           btn.style.display = "block";}
//     }

// // Localisation
// function expandlocalisationOption() {
//       var opt = document.getElementById("localisationOption");
//       var btn = document.getElementById("localisationButton")
//       if (opt.style.display == "none"){
//           opt.style.display = "block";
//           btn.style.display = "none";}
//   }

// function reducelocalisationOption() {
//       var opt = document.getElementById("localisationOption");
//       var btn = document.getElementById("localisationButton")
//       if (opt.style.display == "block"){
//           opt.style.display = "none";
//           btn.style.display = "block";}
//     }

// // diploma
// function expanddiplomaOption() {
//       var opt = document.getElementById("diplomaOption");
//       var btn = document.getElementById("diplomaButton")
//       if (opt.style.display == "none"){
//           opt.style.display = "block";
//           btn.style.display = "none";}
//   }

// function reducediplomaOption() {
//       var opt = document.getElementById("diplomaOption");
//       var btn = document.getElementById("diplomaButton")
//       if (opt.style.display == "block"){
//           opt.style.display = "none";
//           btn.style.display = "block";}
//     }


// // work status
// function expandwork_statusOption() {
//       var opt = document.getElementById("work_statusOption");
//       var btn = document.getElementById("work_statusButton")
//       if (opt.style.display == "none"){
//           opt.style.display = "block";
//           btn.style.display = "none";}
//   }

// function reducework_statusOption() {
//       var opt = document.getElementById("work_statusOption");
//       var btn = document.getElementById("work_statusButton")
//       if (opt.style.display == "block"){
//           opt.style.display = "none";
//           btn.style.display = "block";}
//     }


// // work experience
// function expandwork_experienceOption() {
//       var opt = document.getElementById("work_experienceOption");
//       var btn = document.getElementById("work_experienceButton")
//       if (opt.style.display == "none"){
//           opt.style.display = "block";
//           btn.style.display = "none";}
//   }

// function reducework_experienceOption() {
//       var opt = document.getElementById("work_experienceOption");
//       var btn = document.getElementById("work_experienceButton")
//       if (opt.style.display == "block"){
//           opt.style.display = "none";
//           btn.style.display = "block";}
//     }

// // language
// function expandlanguageOption() {
//       var opt = document.getElementById("languageOption");
//       var btn = document.getElementById("languageButton")
//       if (opt.style.display == "none"){
//           opt.style.display = "block";
//           btn.style.display = "none";}
//   }

// function reducelanguageOption() {
//       var opt = document.getElementById("languageOption");
//       var btn = document.getElementById("languageButton")
//       if (opt.style.display == "block"){
//           opt.style.display = "none";
//           btn.style.display = "block";}
//     }
