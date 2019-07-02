// background image top
function changeBackgroundHeight(x) {
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

    if (width < x) {
        $(".ehHomeOneMobile").css("height", 10+(height/2));}
    else {
        $(".ehHomeOneLaptop").css("height", 150+height-(2 * 50));} }


// mobile inscription button go down
$(function(){
    $( ".inscriptionMobileButton" ).on('click', function(e){
         e.preventDefault();
        $('html, body').animate({scrollTop:$('#ehHomeQuestMobile').offset().top-50}, 'slow');
            return false; }); });


// disable aos on small screen
function swapAOS(x) {
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

    if (width < x) {
        $('div[data-aos="fade-right"]').removeAttr("data-aos").removeAttr("data-aos-duration").removeAttr("data-aos-delay").addClass("aosRight");
        $('div[data-aos="fade-left"]').removeAttr("data-aos").removeAttr("data-aos-duration").removeAttr("data-aos-delay").addClass("aosLeft");}
    else {
        $('aosRight').removeClass("aosRight").attr("data-aos","fade-right").attr("data-aos-duration", "2000").attr("data-aos-delay", "0");
        $('.aosLeft').removeClass("aosRight").attr("data-aos","fade-left").attr("data-aos-duration", "2000").attr("data-aos-delay", "0");}  }


// hide /show top header for small screen + quest mobile at bottom
function swapLaptop(x){
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

    if (width < x) {
        $('.ehHomeOneLaptop').hide();
        $('.ehHomeOneMobile').show();
        $('#ehHomeQuestMobile').show()}
    else {
        $('.ehHomeOneLaptop').show();
        $('.ehHomeOneMobile').hide();
        $('#ehHomeQuestMobile').hide();   }  }

// main
$(function(){
    changeBackgroundHeight(992);
    swapLaptop(992);
    swapAOS(992)
    $(window).resize(function() {
        changeBackgroundHeight(992);
        swapLaptop(992);
        swapAOS(992)}) ;   })



// // inscription button
// // $(document).ready(function(){
// //   $(".ehInscription").mouseover(function(){
// //     $(this).css("background-color", "var(--myBlue)")
// //     .css("color", "var(--myWhite)");
// //   });
// //   $(".ehInscription").mouseout(function(){
// //     $(this).css("background-color", "var(--myWhite)")
// //     .css("color", "var(--myBlue)");
// //   });
// // });



// // function rechercheAction(){
// //     $("#rechercheButton").click(function(){
// //         alert("rechercheButton")
// //         $('#rechercheContent').slideUp();
// //         $('#ecouteContent').slideUp();
// //         $('#rechercheContent').slideDown();    });  }

// // HOME
// // recherche et ecoute
// // $(document).ready(function(){
// //     $("#rechercheButton").click(function(){
// //         if ($('#ecouteContent').css('display') == 'none') {
// //             $('#rechercheContent').hide();
// //             $('#rechercheContent').slideDown();    }
// //         else{
// //             $('#ecouteContent').hide();
// //             $('#rechercheContent').slideDown();    }     });
// //     $("#ecouteButton").click(function(){
// //         if ($('#rechercheContent').css('display') == 'none') {
// //             $('#ecouteContent').hide();
// //             $('#ecouteContent').slideDown();    }
// //         else{
// //             $('#rechercheContent').hide();
// //             $('#ecouteContent').slideDown();    }     });    });


// // APROPOS
// // deja dit
// $(document).ready(function(){
//     $(".dejaDitButton1").click(function(){
//         $('.dejaDitRow2').slideDown();
//         $('.dejaDitButton1').slideUp();    });

//     $(".dejaDitButton2").click(function(){
//         $('.dejaDitRow2').slideUp();
//         $('.dejaDitButton1').slideDown();    });    });


// // APROPOS
// // fin
// $(document).ready(function(){
//     $(".finButton1").click(function(){
//         $('.finRow2').slideDown();
//         $('.finButton1').slideUp();    });

//     $(".finButton2up").click(function(){
//         $('.finRow2').slideUp();
//         $('.finButton1').slideDown();    });

//     $(".finButton2down").click(function(){
//         $('.finRow3').slideDown();
//         $('.finButton2up').slideUp();
//         $('.finButton2down').slideUp();    });

//     $(".finButton3").click(function(){
//         $('.finRow3').slideUp();
//         $('.finButton2up').slideDown();
//         $('.finButton2down').slideDown();    });    });


// // // FAq
// // // oui
// // $(document).ready(function(){
// //     $(".ouiButton1").click(function(){
// //         $('.ouiRow2').slideDown();
// //         $('.ouiButton1').slideUp();    });

// //     $(".ouiButton2up").click(function(){
// //         $('.ouiRow2').slideUp();
// //         $('.ouiButton1').slideDown();    });

// //     $(".ouiButton2down").click(function(){
// //         $('.ouiRow3').slideDown();
// //         $('.ouiButton2up').slideUp();
// //         $('.ouiButton2down').slideUp();    });

// //     $(".ouiButton3up").click(function(){
// //         $('.ouiRow3').slideUp();
// //         $('.ouiButton2up').slideDown();
// //         $('.ouiButton2down').slideDown();    });

// //     $(".ouiButton3down").click(function(){
// //         $('.ouiRow4').slideDown();
// //         $('.ouiButton3up').slideUp();
// //         $('.ouiButton3down').slideUp();    });

// //     $(".ouiButton4").click(function(){
// //         $('.ouiRow4').slideUp();
// //         $('.ouiButton3up').slideDown();
// //         $('.ouiButton3down').slideDown();    });    });


// // QUESTIONNAIRE
// $(document).ready(function(){
//     $("#ehSmartHuntButton").click(function(){
//         $('#ehSmartHuntContent').slideDown();
//         $('#starsOne').slideDown();
//         $('#ehSmartHuntButton').slideUp();   });

//     $("#ehBigHuntButton").click(function(){
//         $('#ehBigHuntContent').slideDown();
//         $('#starsTwo').slideDown();
//         $('#ehBigHuntButton').slideUp();   });

//     $("#ehProHuntButton").click(function(){
//         $('#ehProHuntContent').slideDown();
//         $('#starsThree').slideDown();
//         $('#ehProHuntButton').slideUp();   });   });


// // QUESTIONNAIRE
// function swapConcurrencyDisplay() {
//         var block = document.getElementById("fondConcurency");
//         var d = document.forms[0].fond_already.value;
//         if (d =="Oui")  {
//                     $('#fondConcurency').slideDown() ; }
//         else {
//                     $('#fondConcurency').slideUp() ; }    }

// // QUESTIONNAIRE
// function swapContractDisplay() {
//         var block = document.getElementById("contractBlock");
//         var d = document.forms[0].employed.value;
//         // alert("d is " + d)
//         if (d =="Oui")  {
//                     $('#contractBlock').slideDown() ; }
//         else {
//                     $('#contractBlock').slideUp() ; }    }


// // $(document).ready(function(){
// //     var block = document.getElementById("contractBlock");
// //     var d = document.forms[0].employed.value;
// //     d.addEventListener("change", function() {
// //         if (d =="Non") {
// //             alert("Non");
// //             block.style.display = "none" ;  }
// //         else {
// //             alert("Oui");
// //             block.style.display = "block" ; }    }, false );    })


// // ALLL FADEOUT WHEN LEAVE THE PAHE
// // $(document).ready(function(){
// //     $("a").click(function() {
// //         $("div").fadeOut(300); })   ;})

// // $(document).ready(function(){
// //         $("div").fadeIn(500);   ;})



// // A PROPOS
// $(document).ready(function(){
//     var width = window.innerWidth
//     || document.documentElement.clientWidth
//     || document.body.clientWidth;

//     var height = window.innerHeight
//     || document.documentElement.clientHeight
//     || document.body.clientHeight;

//     if (width > 576) {
//         $("#faitButtonLaptop").mouseover(function(){
//             $('#defaultContentLaptop').hide();
//             $('#faitContentLaptop').show();    });
//         $("#faitButtonLaptop").mouseout(function(){
//             $('#faitContentLaptop').hide();
//             $('#defaultContentLaptop').show();    });
//         $("#cadButtonLaptop").mouseover(function(){
//             $('#defaultContentLaptop').hide();
//             $('#cadContentLaptop').show();    });
//         $("#cadButtonLaptop").mouseout(function(){
//             $('#cadContentLaptop').hide();
//             $('#defaultContentLaptop').show();    });
//         $("#marcheButtonLaptop").mouseover(function(){
//             $('#defaultContentLaptop').hide();
//             $('#marcheContentLaptop').show();    });
//         $("#marcheButtonLaptop").mouseout(function(){
//             $('#marcheContentLaptop').hide();
//             $('#defaultContentLaptop').show();    });        }
//     else{
//        $("#faitButtonMobile").click(function(){
//         if ( 'none' == $('#faitContentMobile').css("display")) {
//             $('#faitContentMobile').slideDown();    }
//         else {
//             $('#faitContentMobile').slideUp();    } } );
//        $("#cadButtonMobile").click(function(){
//         if ( 'none' == $('#cadContentMobile').css("display")) {
//             $('#cadContentMobile').slideDown();    }
//         else {
//             $('#cadContentMobile').slideUp();    } } );
//        $("#marcheButtonMobile").click(function(){
//         if ( 'none' == $('#marcheContentMobile').css("display")) {
//             $('#marcheContentMobile').slideDown();    }
//         else {
//             $('#marcheContentMobile').slideUp();    }    });   }    });

















