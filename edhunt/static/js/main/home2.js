// inscription button
// $(document).ready(function(){
//   $(".ehInscription").mouseover(function(){
//     $(this).css("background-color", "var(--myBlue)")
//     .css("color", "var(--myWhite)");
//   });
//   $(".ehInscription").mouseout(function(){
//     $(this).css("background-color", "var(--myWhite)")
//     .css("color", "var(--myBlue)");
//   });
// });


// GENERAL
// inscription
$(document).ready(function(){
    $(".ehInscriptionSmall").mouseover(function(){
        $(this).css("background-color", "var(--myBrown)")
        .css("color", "var(--myWhite)");     });
    $(".ehInscriptionSmall").mouseout(function(){
        $(this).css("background-color", "var(--myWhite)")
        .css("color", "var(--myBrown)");    });  });


// GENERAL
// ehTextBoxGridNeuf
$(document).ready(function(){
  $(".ehTextBoxGridNeuf").mouseover(function(){
    $(this).css("background-color", "var(--myBrown)")
    .css("color", "var(--myWhite)");
  });
  $(".ehTextBoxGridNeuf").mouseout(function(){
    $(this).css("background-color", "var(--myWhite)")
    .css("color", "var(--myBrown)");
  });
});


// GENERAL
// ehTextBox3
$(document).ready(function(){
  $(".ehTextBox3").mouseover(function(){
    $(this).css("background-color", "var(--myBrown)")
    .css("color", "var(--myWhite)");
  });
  $(".ehTextBox3").mouseout(function(){
    $(this).css("background-color", "var(--myWhite)")
    .css("color", "var(--myBrown)");
  });
});

// $(document).ready(function(){
//   $(".ehTextBoxTop").mouseover(function(){
//     $(this).css("background-color", "var(--myBrown)")
//     .css("color", "var(--myWhite)");
//   });
//   $(".ehTextBoxTop").mouseout(function(){
//     $(this).css("background-color", "var(--myWhite)")
//     .css("color", "var(--myBrown)");
//   });
// });


// GENERAL
// foot
$(document).ready(function(){
    $(".ehTextBoxFoot").mouseover(function(){
        $(this).css("background-color", "var(--myBrown)")
        .css("color", "var(--myWhite)");     });
    $(".ehTextBoxFoot").mouseout(function(){
        $(this).css("background-color", "var(--myWhite)")
        .css("color", "var(--myBrown)");    });   });



// HOME
// recherche et ecoute
$(document).ready(function(){
    $("#rechercheButton").mouseover(function(){
        $('#defaultContent').hide();
        $('#rechercheContent').show();    });
    $("#rechercheButton").mouseout(function(){
        $('#rechercheContent').hide();
        $('#defaultContent').show();    });
    $("#ecouteButton").mouseover(function(){
        $('#defaultContent').hide();
        $('#ecouteContent').show();    });
    $("#ecouteButton").mouseout(function(){
        $('#ecouteContent').hide();
        $('#defaultContent').show();    });   });


// APROPOS
// deja dit
$(document).ready(function(){
    $(".dejaDitButton1").click(function(){
        $('.dejaDitRow2').slideDown();
        $('.dejaDitButton1').slideUp();    });

    $(".dejaDitButton2").click(function(){
        $('.dejaDitRow2').slideUp();
        $('.dejaDitButton1').slideDown();    });    });


// APROPOS
// fin
$(document).ready(function(){
    $(".finButton1").click(function(){
        $('.finRow2').slideDown();
        $('.finButton1').slideUp();    });

    $(".finButton2up").click(function(){
        $('.finRow2').slideUp();
        $('.finButton1').slideDown();    });

    $(".finButton2down").click(function(){
        $('.finRow3').slideDown();
        $('.finButton2up').slideUp();
        $('.finButton2down').slideUp();    });

    $(".finButton3").click(function(){
        $('.finRow3').slideUp();
        $('.finButton2up').slideDown();
        $('.finButton2down').slideDown();    });    });


// FAq
// oui
$(document).ready(function(){
    $(".ouiButton1").click(function(){
        $('.ouiRow2').slideDown();
        $('.ouiButton1').slideUp();    });

    $(".ouiButton2up").click(function(){
        $('.ouiRow2').slideUp();
        $('.ouiButton1').slideDown();    });

    $(".ouiButton2down").click(function(){
        $('.ouiRow3').slideDown();
        $('.ouiButton2up').slideUp();
        $('.ouiButton2down').slideUp();    });

    $(".ouiButton3up").click(function(){
        $('.ouiRow3').slideUp();
        $('.ouiButton2up').slideDown();
        $('.ouiButton2down').slideDown();    });

    $(".ouiButton3down").click(function(){
        $('.ouiRow4').slideDown();
        $('.ouiButton3up').slideUp();
        $('.ouiButton3down').slideUp();    });

    $(".ouiButton4").click(function(){
        $('.ouiRow4').slideUp();
        $('.ouiButton3up').slideDown();
        $('.ouiButton3down').slideDown();    });    });


// QUESTIONNAIRE
$(document).ready(function(){
    $("#ehSmartHuntButton").click(function(){
        $('#ehSmartHuntContent').slideDown();
        $('#starsOne').slideDown();
        $('#ehSmartHuntButton').slideUp();   });

    $("#ehBigHuntButton").click(function(){
        $('#ehBigHuntContent').slideDown();
        $('#starsTwo').slideDown();
        $('#ehBigHuntButton').slideUp();   });

    $("#ehProHuntButton").click(function(){
        $('#ehProHuntContent').slideDown();
        $('#starsThree').slideDown();
        $('#ehProHuntButton').slideUp();   });   });


// QUESTIONNAIRE
function swapConcurrencyDisplay() {
        var block = document.getElementById("fondConcurency");
        var d = document.forms[0].fond_already.value;
        if (d =="Oui")  {
                    $('#fondConcurency').slideDown() ; }
        else {
                    $('#fondConcurency').slideUp() ; }    }

// QUESTIONNAIRE
function swapContractDisplay() {
        var block = document.getElementById("contractBlock");
        var d = document.forms[0].employed.value;
        // alert("d is " + d)
        if (d =="Oui")  {
                    $('#contractBlock').slideDown() ; }
        else {
                    $('#contractBlock').slideUp() ; }    }


// $(document).ready(function(){
//     var block = document.getElementById("contractBlock");
//     var d = document.forms[0].employed.value;
//     d.addEventListener("change", function() {
//         if (d =="Non") {
//             alert("Non");
//             block.style.display = "none" ;  }
//         else {
//             alert("Oui");
//             block.style.display = "block" ; }    }, false );    })




// A PROPOS
$(document).ready(function(){
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

    var height = window.innerHeight
    || document.documentElement.clientHeight
    || document.body.clientHeight;

    if (width > 576) {
        $("#faitButtonLaptop").mouseover(function(){
            $('#defaultContentLaptop').hide();
            $('#faitContentLaptop').show();    });
        $("#faitButtonLaptop").mouseout(function(){
            $('#faitContentLaptop').hide();
            $('#defaultContentLaptop').show();    });
        $("#cadButtonLaptop").mouseover(function(){
            $('#defaultContentLaptop').hide();
            $('#cadContentLaptop').show();    });
        $("#cadButtonLaptop").mouseout(function(){
            $('#cadContentLaptop').hide();
            $('#defaultContentLaptop').show();    });
        $("#marcheButtonLaptop").mouseover(function(){
            $('#defaultContentLaptop').hide();
            $('#marcheContentLaptop').show();    });
        $("#marcheButtonLaptop").mouseout(function(){
            $('#marcheContentLaptop').hide();
            $('#defaultContentLaptop').show();    });        }
    else{
       $("#faitButtonMobile").click(function(){
        if ( 'none' == $('#faitContentMobile').css("display")) {
            $('#faitContentMobile').slideDown();    }
        else {
            $('#faitContentMobile').slideUp();    } } );
       $("#cadButtonMobile").click(function(){
        if ( 'none' == $('#cadContentMobile').css("display")) {
            $('#cadContentMobile').slideDown();    }
        else {
            $('#cadContentMobile').slideUp();    } } );
       $("#marcheButtonMobile").click(function(){
        if ( 'none' == $('#marcheContentMobile').css("display")) {
            $('#marcheContentMobile').slideDown();    }
        else {
            $('#marcheContentMobile').slideUp();    }    });   }    });



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



// A PROPOS
function dejaDitFunct(item){
        $("#dejaDitButton"+item).mouseover(function(){
            $('#dejaDitKeyContent'+item).hide();
            $('#dejaDitValContent'+item).show();    });
        $("#dejaDitButton"+item).mouseout(function(){
            $('#dejaDitValContent'+item).hide();
            $('#dejaDitKeyContent'+item).show();    });   ;}



// A PROPOS
// deja dit
$(document).ready(function(){
    dejaDitFunct(1);
    dejaDitFunct(2);
    dejaDitFunct(3);
    dejaDitFunct(4);
    dejaDitFunct(5);
    dejaDitFunct(6);    });




function ouiFunct(item){
        $("#ouiButton"+item).mouseover(function(){
            $('#ouiKeyContent'+item).hide();
            $('#ouiValContent'+item).show();    });
        $("#ouiButton"+item).mouseout(function(){
            $('#ouiValContent'+item).hide();
            $('#ouiKeyContent'+item).show();    });   ;}



// A PROPOS
// deja dit
$(document).ready(function(){
    ouiFunct(1);
    ouiFunct(2);
    ouiFunct(3);
    ouiFunct(4);
    ouiFunct(5);
    ouiFunct(6);
    ouiFunct(7);
    ouiFunct(8);
    ouiFunct(9);
    ouiFunct(10);
    ouiFunct(11);
    ouiFunct(12);    });


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


function swapOrder576() {
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

    var height = window.innerHeight
    || document.documentElement.clientHeight
    || document.body.clientHeight;
    if (width < 576) {
        $(".swap576").addClass("order-first");}
    else {
        $(".swap576").removeClass("order-first");}  }


// main
$(function(){
    hide576();
    show576();
    showResponsiveTopBox();
    manageResponsiveBlock();
    swapOrder576();
    $(window).resize(function() {
        hide576();
        show576();
        showResponsiveTopBox();
        manageResponsiveBlock();
        swapOrder576(); })    })



